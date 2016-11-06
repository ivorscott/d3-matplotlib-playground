Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network :forwarded_port, guest: 8000, host: 8000, host_ip: "127.0.0.1"
  config.vm.synced_folder "." , "/home/vagrant"
  config.vm.provision :shell, :path => "boot.sh", run: "always"
  config.vm.post_up_message = "The application is available at http://127.0.0.1:8000"
end

