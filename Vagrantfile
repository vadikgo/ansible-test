Vagrant.configure(2) do |config|

  config.vm.box = "boxcutter/ol67"

  provider = (ARGV[2] || ENV['VAGRANT_DEFAULT_PROVIDER'] || :virtualbox).to_sym

  if provider == :virtualbox
      config.vm.provider "virtualbox" do |vb|
        vb.gui = false
        vb.memory = "1024"
      end
  end

  if provider == :parallels
      config.vm.provider "parallels" do |prl|
        prl.memory = "1024"
        prl.name = "test1"
        prl.linked_clone = true
        prl.update_guest_tools = false
        prl.check_guest_tools = false
      end
  end

  config.vm.hostname = "test1"
  config.vm.network :forwarded_port, guest: 8088, host: 8088 # storm ui

#  config.vm.provision "shell", inline: <<-SHELL
#     sudo yum update -y
#  SHELL

  #config.vm.provision "shell", inline: "yum install libselinux-python -y"
  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "playbook.yml"
  end
end
