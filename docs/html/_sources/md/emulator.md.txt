# Qristal Emulator Getting Started Guide

## 1. Check that your system meets minimum requirements

- 16 GB RAM
- x86 processor
- A working Linux system. Windows Subsystem for Linux 2 (WSL) is fine.

## 2. Install Docker

Instructions for installing Docker can be found [here](https://docs.docker.com/engine/install/).  You only need the Engine, not the Desktop.

If you have NVIDIA GPUs on your system and want to use them, you will also need to install the [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-docker).

## 3. Log in to the Gitlab Docker registry

Open a terminal and run:
```shell
sudo docker login -u XXXX registry.gitlab.com
```
where `XXXX` is replaced with your Gitlab username.  Depending on your Gitlab authentication settings, you may need to work through getting a token and/or setting up two-factor authentication.  If you have trouble, please refer to [this guide](https://docs.gitlab.com/ee/user/packages/container_registry/authenticate_with_container_registry.html).

## 4. Get the Qristal Emulator Image

In a terminal, run:
```shell
sudo docker run --rm -it --name emulator registry.gitlab.com/qbau/software-and-apps/public-restricted/emulator/qristal-emulator
```
If you have NVIDIA GPUs on your system and want to use them, insert `--gpus all` after `run` in the command above.

## 5. Activate the image using your license key

At the command prompt _inside the image_, run the following commands, replacing `XXXXX-XXXXX-XXXXX-XXXXX` with the license key that you have received from Quantum Brilliance:
```shell
mkdir /qristal
echo -e '{\n  "isFloatingLicense": true,\n  "LicenseKey": "XXXXX-XXXXX-XXXXX-XXXXX"\n}' > /qristal/Qristal-Emulator-License.json
```

## 6. Test that your image is successfully activated

Navigate to the Python examples folder in the image
```shell
cd /mnt/qb/qristal/examples/python
```

Run a simple example that uses a noise model.  First, using a noise model that is built into the open-source version of Qristal and does not require an emulator license:
```shell
python3 noise_model.py
```

Next, retry the example using a noise model imported from the emulator:
```shell
python3 noise_model.py --qdk
```
You should see something similar to the following:
```shell
Running in virtual machine: enforcing floating license!

Retrieving license-key and floating-setting from json file: /qristal/Qristal-Emulator-License.json
{
    "LicenseKey": "XXXXX-XXXXX-XXXXX-XXXXX",
    "isFloatingLicense": true
}
Provided floating license, key: XXXXX-XXXXX-XXXXX-XXXXX, productID: 20053 and machine code: floating-7943610145998300972
Provided floating license, key: XXXXX-XXXXX-XXXXX-XXXXX, productID: 20053 and machine code: floating-7943610145998300972
{
    "00": 274,
    "01": 247,
    "10": 234,
    "11": 269
}
```

## 7. Run some other examples

1. Go to the Python examples folder in the image: `cd /mnt/qb/qristal/examples/python`
2. Run example `qb_statevector_noisy.py` using `python3 qb_statevector_noisy.py`. You should get the output:
```shell
{'110': 1024}
```
4. Install the text editor `nano` to edit the noise properties using `apt install nano`.
5. Open `qb_statevector_noisy.py` with the text editor `nano` using `nano qb_statevector_noisy.py`
6. Within the text editor, turn on noise properties by uncommenting lines
    - ```python
      s.noise = True
      ```
    - ```python
      s.noise_model = qristal.core.NoiseModel("qb-nm1", n_qbits)
      ```
7. Exit the text editor by hitting `Ctrl + x`, then enter `y` to save changes, then hit `Enter`.
8. Rerun the example using the same command `python3 qb_statevector_noisy.py`. You should see something similar to this output:
```shell
Running in virtual machine: enforcing floating license!

Retrieving license-key and floating-setting from json file: /qristal/Qristal-Emulator-License.json
{
    "LicenseKey": "XXXXX-XXXXX-XXXXX-XXXXX",
    "isFloatingLicense": true
}
Provided floating license, key: XXXXX-XXXXX-XXXXX-XXXXX, productID: 20053 and machine code: floating-5076244496556924759
Provided floating license, key: XXXXX-XXXXX-XXXXX-XXXXX, productID: 20053 and machine code: floating-5076244496556924759
{'000': 1, '010': 18, '100': 7, '110': 982, '111': 16}
```
9. Try out a C++ example with CUDA Quantum.  Navigate to the example folder:
```shell
cd /mnt/qb/qristal/examples/cpp/benchmark1_cudaq/
```

10. Build and run the example:

```shell
mkdir build
cd build
cmake ..
make
./benchmark1_cudaq
```
You should get results that look similar to this:
```shell
Executing C++ demo...
About to run quantum program...
Results:
{
    "00000000000000000000": 10038,
    "11111111111111111111": 9962
}
```

11. Try out some of the other examples in `/mnt/qb/qristal/examples`.  Note that a few of these (e.g. `cudaq_qft`) use simulators that only work with GPUs, so if you're not running with GPUs these particular examples won't execute.


## 8. Test out the Jupyter Lab interface, and try the exercise

1. Launch Jupyter Lab by opening up your browser and typing in the navigator `localhost:8889`.
2. Make a new notebook, and try executing one of the python examples in it.
3. Open `/mnt/qb/qristal/exercises/QB_Qristal_Challenge/QB_Qristal_Challenge.ipynb` inside Jupyter Lab, and see if you can solve the problems there!  If you struggle, you can find solutions in the same directory.

## 9. Write your own quantum programs!

We'd love to hear how you get on -- let your sales contact know!

## 10. Known issues

The following are known issues under active development:

- When using Cudaq-wrapped tensor network backends `cudaq:qb_mps`, `cudaq:qb_purification` and `cudaq:qb_mpdo`, all qubits in the circuit need to be measured. The measurement order of the qubits needs to be in increasing order of the qubit index. Only if these guidelines are followed will bitstring output registers from these backends be consistent with the outputs of other backends.