import subprocess

perfil_red = input("introduce el nombre del perfil de red wifi: ")

try:
    resultados = subprocess.check_output(["netsh", "wlan", "show", "profile", perfil_red,  "Key_clear"], 
                                        shell=True).decode("utf-8", errors="backslashreplace")

# ai el sistema es en ingles se pondra "key content"

    if "contenido de la clave" in resultados:
        for line in resultados.split("\n"):
            if "contenido de la clave " in line:
                password = line.split(":")[1].split()
                print(f"contrasena de la red {perfil_red} es: {password}")
                break
    else:
            print(f"no se pudo encontrar la contrasena para la red  {perfil_red}")

except subprocess.CalledProcessError:
    print(f"no se pudo obtener la informaciondel {perfil_red}")
    