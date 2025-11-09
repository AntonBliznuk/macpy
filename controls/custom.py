import subprocess


def cloudflare_warp_connection(activate: bool = True) -> None:
    try:
        state = "connect" if activate else "disconnect"
        subprocess.run(
            ["warp-cli", state],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"✅ Cloudflare warp connection {'enabled' if activate else 'disabled'}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to change cloudflare warp connection state: {e}")


# Here you can add your custom controllers.

if __name__ == "__main__":
    cloudflare_warp_connection(False)

