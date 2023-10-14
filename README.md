# listening

List processes listening for network connections. `listening` is an easier-to-use, cross-platform (Linux and macOS) wrapper for `lsof` and `netstat`, with a consistent user interface.

## Usage

```text
listening [OPTIONS]
```

### Options

- `-p PORT`, `--port PORT`: Filter to processes listening on the given port. Default: none (all ports).
- `-t {tcp,udp}`, `--transport {tcp,udp}`: Specifies TCP or UDP. Default: none (both).
- `-i {4,6}`, `--ip {4,6}`: Specifies IPv4 or IPv6. Default: none (both).
- `-h`, `--help`: Print help and exit.
- `-v`, `--version`: Print version and exit.
- `-d DEBUG`, `--debug DEBUG`: Whether to print (to stderr) the `lsof`/`netstat` command to be executed. Default: False.

## Installation

### macOS via Homebrew

```shell
brew install cdzombak/oss/listening
```

### Debian via apt repository

Install my Debian repository if you haven't already:

```shell
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://dist.cdzombak.net/deb.key | sudo gpg --dearmor -o /etc/apt/keyrings/dist-cdzombak-net.gpg
sudo chmod 0644 /etc/apt/keyrings/dist-cdzombak-net.gpg
echo -e "deb [signed-by=/etc/apt/keyrings/dist-cdzombak-net.gpg] https://dist.cdzombak.net/deb/oss any oss\n" | sudo tee -a /etc/apt/sources.list.d/dist-cdzombak-net.list > /dev/null
sudo apt-get update
```

Then install `listening` via `apt-get`:

```shell
sudo apt-get install listening
```

### Manual installation from build artifacts

Pre-built binaries for are downloadable from each [GitHub Release](https://github.com/cdzombak/listening/releases). Debian packages for each release are available as well.

### Build and install locally

```shell
git clone https://github.com/cdzombak/listening.git
cd listening
make build

cp out/listening-[VERSION]-all $INSTALL_DIR/listening
```

## About

- Issues: https://github.com/cdzombak/listening/issues/new
- Author: [Chris Dzombak](https://www.dzombak.com)
  - [GitHub: @cdzombak](https://www.github.com/cdzombak)

## License

LGPLv3; see `LICENSE` in this repository.
