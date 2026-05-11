#!/usr/bin/env python3
import json
import os
import sys
from pathlib import Path

import click

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.crypto import make_fernet
from app.store import export_suppressions, import_suppressions, list_users, create_user, delete_user, get_user, update_user_api_key
from app.auth import hash_password


@click.group()
def cli():
    pass


@cli.command()
def keygen():
    import secrets
    secret = secrets.token_hex(32)
    api_key = secrets.token_hex(16)
    click.echo(f"SECRET_KEY={secret}")
    click.echo(f"ADMIN_API_KEY={api_key}")
    click.echo("\nAdd these to your .env file.")


@cli.command()
@click.option("--file", "-f", default="data/suppressions.enc")
def export(file):
    os.environ["SUPPRESSION_FILE"] = file
    secret = os.environ.get("SECRET_KEY")
    if not secret:
        click.echo("SECRET_KEY env var required", err=True)
        sys.exit(1)
    fernet = make_fernet(secret)
    data = export_suppressions(fernet)
    click.echo(json.dumps(data, indent=2))


@cli.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.option("--file", "-f", default="data/suppressions.enc")
def import_cmd(input_file, file):
    os.environ["SUPPRESSION_FILE"] = file
    secret = os.environ.get("SECRET_KEY")
    if not secret:
        click.echo("SECRET_KEY env var required", err=True)
        sys.exit(1)
    fernet = make_fernet(secret)
    with open(input_file) as f:
        data = json.load(f)
    count = import_suppressions(fernet, data)
    click.echo(f"Imported {count} suppressions")


@cli.command()
@click.option("--file", "-f", default="data/suppressions.enc")
def stats(file):
    os.environ["SUPPRESSION_FILE"] = file
    secret = os.environ.get("SECRET_KEY")
    if not secret:
        click.echo("SECRET_KEY env var required", err=True)
        sys.exit(1)
    fernet = make_fernet(secret)
    store = export_suppressions(fernet)
    supps = store.get("suppressions", {})
    users = store.get("users", {})
    click.echo(f"Users:           {len(users)}")
    click.echo(f"Suppressions:    {len(supps)}")
    click.echo(f"  Global:        {sum(1 for v in supps.values() if v.get('global'))}")
    click.echo(f"  Network:       {sum(1 for v in supps.values() if v.get('networks'))}")
    click.echo(f"  Offer:         {sum(1 for v in supps.values() if v.get('offers'))}")


@cli.group()
def user():
    pass


@user.command("create")
@click.argument("email")
@click.argument("password")
@click.option("--role", default="user", type=click.Choice(["admin", "user"]))
@click.option("--file", "-f", default="data/suppressions.enc")
def user_create(email, password, role, file):
    os.environ["SUPPRESSION_FILE"] = file
    secret = os.environ.get("SECRET_KEY")
    if not secret:
        click.echo("SECRET_KEY env var required", err=True)
        sys.exit(1)
    fernet = make_fernet(secret)
    pw_hash = hash_password(password)
    user = create_user(fernet, email, pw_hash, role)
    click.echo(f"Created: {user.email} ({user.role})")


@user.command("delete")
@click.argument("email")
@click.option("--file", "-f", default="data/suppressions.enc")
def user_delete(email, file):
    os.environ["SUPPRESSION_FILE"] = file
    secret = os.environ.get("SECRET_KEY")
    if not secret:
        click.echo("SECRET_KEY env var required", err=True)
        sys.exit(1)
    fernet = make_fernet(secret)
    if delete_user(fernet, email):
        click.echo(f"Deleted: {email}")
    else:
        click.echo(f"User not found: {email}", err=True)
        sys.exit(1)


@user.command("list")
@click.option("--file", "-f", default="data/suppressions.enc")
def user_list(file):
    os.environ["SUPPRESSION_FILE"] = file
    secret = os.environ.get("SECRET_KEY")
    if not secret:
        click.echo("SECRET_KEY env var required", err=True)
        sys.exit(1)
    fernet = make_fernet(secret)
    users = list_users(fernet)
    if not users:
        click.echo("No users found")
        return
    for u in users:
        click.echo(f"{u.email:30s} {u.role:6s} api_key={u.api_key}")


@user.command("reset-api-key")
@click.argument("email")
@click.option("--file", "-f", default="data/suppressions.enc")
def reset_api_key(email, file):
    os.environ["SUPPRESSION_FILE"] = file
    secret = os.environ.get("SECRET_KEY")
    if not secret:
        click.echo("SECRET_KEY env var required", err=True)
        sys.exit(1)
    fernet = make_fernet(secret)
    new_key = update_user_api_key(fernet, email)
    click.echo(f"New API key for {email}: {new_key}")


cli.add_command(user)

if __name__ == "__main__":
    cli()
