vm_list = ['test1']

Vagrant.configure(2) do |config|

  vm_list.each_with_index do |vm_name, vm_index|
      config.vm.define vm_name do |vmn|
          vmn.vm.box = "boxcutter/ol67"
          vmn.vm.box_check_update = false

          provider = (ARGV[2] || ENV['VAGRANT_DEFAULT_PROVIDER'] || :virtualbox).to_sym

          if provider == :virtualbox
              vmn.vm.provider "virtualbox" do |vb|
                vb.gui = false
                vb.memory = "1024"
              end
          end

          if provider == :parallels
              vmn.vm.provider "parallels" do |prl|
                prl.memory = "1024"
                prl.name = vm_name
                prl.linked_clone = true
                prl.update_guest_tools = false
                prl.check_guest_tools = false
              end
          end

          vmn.vm.hostname = vm_name
          vmn.vm.network "private_network", ip: "192.168.50.#{2+vm_index}"
          vmn.vm.network :forwarded_port, guest: 8088, host: 8088+vm_index # storm ui

        #  config.vm.provision "shell", inline: <<-SHELL
        #     sudo yum update -y
        #  SHELL

          vmn.vm.provision "ansible" do |ansible|
            ansible.verbose = "v"
            ansible.groups = {
              "zookeeper" => vm_list,
              "storm" => vm_list,
              "all_groups:children" => ["zookeeper", "storm"]
            }
            ansible.playbook = "test.yml"
          end
      end
  end
end
