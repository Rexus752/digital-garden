import os
import shutil
from pathlib import Path

def main():
    main_folder = Path("/home/manuel/Manuel/images/desktop-wallpapers")
    
    if not main_folder.exists():
        print(f"Errore: La cartella '{main_folder}' non esiste.")
        return
    
    file_copiati = 0
    file_ignorati = 0
    
    for root, dirs, files in os.walk(main_folder):
        root_path = Path(root)
        
        if root_path == main_folder:
            continue
        
        for file in files:
            percorso_file = root_path / file
            percorso_destinazione = main_folder / file
            
            try:
                if percorso_destinazione.exists():
                    print(f"Attenzione: Il file '{file}' esiste già. Ignorato.")
                    file_ignorati += 1
                    continue
                
                shutil.copy2(percorso_file, percorso_destinazione)
                print(f"Copiato: {percorso_file}")
                file_copiati += 1
                
            except Exception as e:
                print(f"Errore: {e}")
    
    print(f"\nCopiati: {file_copiati}, Ignorati: {file_ignorati}")

if __name__ == "__main__":
    main()
