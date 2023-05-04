import click
import json
import subprocess, time

# all_colors = ( "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white", "bright_black", "bright_red", "bright_green", "bright_yellow", "bright_blue", "bright_magenta", "bright_cyan", "bright_white", )

# Mulai Perintah
@click.command()
# @click.option("--menu", default="biasalah", help="Nama Pilihan Menu", prompt="Apa cari kak? <enter> ->")
@click.option("--menu", default="basic", help="Nama Pilihan Menu")
@click.option("-r", "--run", "r", type=int, multiple=True, help="Index of the menu to execute")

# Just the main app
def main(menu,r):

    subprocess.run("clear", shell=True)
    
    # Mengambil data menu di file json
    try:
        with open(f"lib/{menu}.json", "r") as f:
            menu_data = json.load(f)
    except FileNotFoundError:
        click.echo(f"Kami gak kenal : {menu}, Apa itu kak? yang benar aja lah -_-")
        click.echo(click.style("Kalau lagi pening? enter aja!", blink=True))
        return
    
    # with open(menu, "r") as f:
    #     menu_data = json.load(f)
   
    # untuk multiple dengan run
    # if r is not None and e is not None:
    #     menu_item = menu_data["menu"][r - 1]
    #     option = menu_item["options"][e - 1]
    #     click.echo(f"Executing command: {option['command']}")
    #     subprocess.run(option["command"], shell=True)
    #     return

    while True:

        # Menampilkan menu pilihan
        click.echo(click.style("=" * 30, fg="red", bold=True))
        click.echo(click.style(menu_data["title"], blink=True))
        click.echo(menu_data["description"])
        click.echo(click.style("=" * 30, fg="red", bold=True))       
        click.echo(" ")

        for i, menu_item in enumerate(menu_data["menu"]):
            click.echo(f"{i+1}. {menu_item['title']}")
        
        click.echo("0. Kelua")
        choice = click.prompt("\nPileh lah", type=int)
        
        if choice == 0:
            subprocess.run("clear", shell=True)
            click.echo("\nNgape kelua? ...")
            click.echo("Tagehkah? Balik lagi ntar boh! ...  \n")
            click.echo(click.style("Jangan lupe bintangnye ^_^ \n", blink=True))
            break

        
        try:
            menu_item = menu_data["menu"][choice - 1]
        except IndexError:
            subprocess.run("clear", shell=True)
            click.echo(" ")
            click.echo(click.style(f"✗ Kami gak kenal pilihan: {choice}, Apa itu kak? yang benar aja lah -_-", fg="yellow", bold=True) )
            click.echo(" ")
            continue

        ## Menu Dalam Pertama
        subprocess.run("clear", shell=True)
        click.echo(click.style("=" * 30, fg="red", bold=True))
        click.echo(menu_data["title"] + " > " + menu_item["title"])
        click.echo("-----> " + menu_item["description"])
        click.echo(click.style("=" * 30, fg="red", bold=True))
        click.echo(" ")
        
        for i, option in enumerate(menu_item["options"]):
            click.echo(f"{i+1}. {option['name']}")
        
        click.echo("0. Balek")
        option_choice = click.prompt("\nPileh lah", type=int)
        
        if option_choice == 0:
            continue

        try:
            option = menu_item["options"][option_choice - 1]
        except IndexError:
            subprocess.run("clear", shell=True)
            click.echo(" ")
            click.echo(click.style(f"✗ Kami gak kenal pilihan: {choice}, Apa itu kak? yang benar aja lah -_-", fg="yellow", bold=True) )
            click.echo(" ")
            continue
    
        click.echo(" ")
        for command in option["command"]:
            click.echo(f"Menjalankan : {command}")
            subprocess.run(command, shell=True)
            

if __name__ == '__main__':
    main()