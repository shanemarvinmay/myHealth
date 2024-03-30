import typer

app = typer.Typer()

@app.command()
def get_nutrition_from_photo(photo_path: str):
    """Upload photo based on file path.
    """    
    print(f"Photo path: {photo_path}")
    with open(photo_path, 'rb') as f:
        photo = f.read()
    print(f"Photo preview:{photo[:50]}")

if __name__ == "__main__":
    app()
