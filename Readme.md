# Setting up

- install [Miniconda](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)
- install create the environment and activate it:
    ```
    conda env create -f environment.yml
    conda activate openaigym
    ```


##  configure headless gpu acceleration 

- prereqs:
    - install nvidia drivers

- get  the  gpu busid

```
nvidia-xconfig --query-gpu-info
```

`
GPU #0:
  Name      : Tesla M60
  ...
  PCI BusID : PCI:136:0:0
`

- create an xorg.conf file for headless operation

```
sudo nvidia-xconfig -a --allow-empty-initial-configuration --use-display-device=None \
--virtual=1920x1200 --busid {busid}
```

- edit `/etc/X11/xorg.conf` and delete the sections ServerLayout and Screen

```
sudo nano /etc/X11/xorg.conf
```

- start an X server and check that it is running on the GPU
    - create `.Xauthority` in your home: `touch ~/.Xauthority`

    ```
    export DISPLAY=:0
    export USER=aldopareja
    sudo Xorg $DISPLAY -auth /home/aldopareja/.Xauthority &
    ```
    
    - test that  the server is  running on GPU, ``nvidia-smi`` output:
        ```
        +-----------------------------------------------------------------------------+
        | Processes:                                                       GPU Memory |
        |  GPU       PID   Type   Process name                             Usage      |
        |=============================================================================|
        |    0     34080      G   /usr/lib/xorg/Xorg                            22MiB |
        +-----------------------------------------------------------------------------+
        ```
    - test that you can use opengl on the  server by running `glxgears`
        - install mesa-utils if the package is  not available:
            `sudo apt install mesa-utils`
        - you  won't see anything but  if it  runs it means the gpu is accelerating frames
    

- start an Xpra server on the display
-  install [xpra](https://xpra.org/trac/wiki/Download#Linux) if necessary

```
xpra start :0 --use-display  
```
- install xpra [locally](https://xpra.org/trac/wiki/Download) for
- on the local machine attach to the xpra session in the remote server (requires having ssh-key set up  or shh password)
```
export USER=aldopareja
xpra attach ssh://$USER@<remote_ip>/0
``` 
- excecute `glxgears` on the server and se gears spinning on your local machine
```
glxgears
```

- test that you can render a simple gym  environmet (should  see  rendering locally):
```
python cart-pole_rendering.py
```




    
