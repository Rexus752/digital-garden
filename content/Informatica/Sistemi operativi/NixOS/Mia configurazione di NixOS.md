
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

Repository di Forgejo: https://forgejo.it/Rexus752/my-nixos-config.

# 1 - Come aggiungere un nuovo dispositivo

Questo in realtà serve più a me che a te, dato che molto probabilmente ti conviene di più copiare una per una le varie parti della configurazione, piuttosto che copiarla interamente.

## 1.1 - Sul vecchio dispositivo

## 1.2 - Sul nuovo dispositivo

1. Installa NixOS
2. Spostati nella cartella `/etc/nixos`:
	```shell
	cd /etc/nixos
	```
3. Apri il terminale e modifica la configurazione:
	```shell
	sudoedit configuration.nix
	```
4. Prendi nota delle impostazioni del bootloader. Nel mio caso corrispondono a:
	```nix
	boot.loader.systemd-boot.enable = true;
	boot.loader.efi.canTouchEfiVariables = true;
	```
5. Aggiungi git tra i pacchetti da installare:
	```nix {4}
	{
	  # ...
	  environment.systemPackages = with pkgs; [
	    git
	  ]
	  # ...
	}
	```
6. Aggiungi queste opzioni per usare nix-command e flakes e per incrementare la dimensione del download buffer a 512MB:
	```nix {3-4}
	{
	  # ...
	  nix.settings.experimental-features = [ "nix-command" "flakes" ];
	  nix.settings.download-buffer-size = 536870912;
	  # ...
	}
	```
7. Fai il rebuild (assicurati di essere conness* a internet):
	```shell
	sudo nixos-rebuild switch
	```
8. Spostare i file di configurazione generati automaticamente da un'altra parte (es. Desktop):
	```shell
	sudo mv * ~/Desktop
	```
9. Clonare il repository in `/etc/nixos` con 
	```shell
	sudo git clone https://forgejo.it/Rexus752/my-nixos-config .
	```
10. Creare in `/devices/` una nuova cartella con il nome del dispositivo (es. `manuel-laptop`):
	```shell
	sudo mkdir devices/manuel-laptop
	```
11. Spostare il file di configurazione `hardware-configuration.nix` generato inizialmente in `devices/manuel-laptop`:
	```shell
	sudo mv ~/Desktop/hardware-configuration.nix devices/manuel-laptop
	```
12. Copiare il `configuration.nix` di uno dei dispositivi già esistenti (es. `manuel-labtop`) al posto di quello di questo:
	```shell
	sudo cp devices/manuel-labtop/configuration.nix devices/manuel-laptop
	```
13. Modificare il `configuration.nix` del dispositivo:
	```shell
	sudoedit devices/manuel-laptop/configuration.nix
	```
14. Cambiare l'hostname:
	```nix {2}
	let
	  hostname = "manuel-laptop";
	in {
	  ...
	```
15. Sostituisci le opzioni del bootloader con quelle che hai salvato prima.
16. Salva le modifiche ed esci
17. Modificare il flake:
	```shell
	sudoedit flake.nix
	```
18. Aggiungere il dispositivo al flake:
	```nix {12-22}
	{
	  # ...
	  outputs = {
		self,
		nixpkgs,
		home-manager,
		sops-nix,
		# temp,
		... }@inputs: {
		nixosConfigurations = {
		  # ...
		  manuel-laptop = nixpkgs.lib.nixosSystem {
			system = "x86_64-linux";
			modules = [
			  ./devices/manuel-laptop/configuration.nix
			  home-manager.nixosModules.default
			  sops-nix.nixosModules.default
			];
			specialArgs = {
			  inherit inputs;
			};
		  };
		};
	  };
	}
	```
19. Eseguire il rebuild specificando di usare la configurazione del nuovo dispositivo:
	```shell
	sudo git add .
	sudo nixos-rebuild switch --flake /etc/nixos/#manuel-laptop
	```
20. Riavvia il computer
21. Su forgejo.it genera una nuova chiave SSH e aggiungila alle chiavi dell'account di forgejo.it
22. Cambia il remote del repository in quello SSH
23. Esegui
	```shell
	sudo chown -R manuel:users /etc/nixos
	```
