word_size = 32
num_words = 512
write_size = 8

num_rw_ports = 1
num_r_ports = 1
num_w_ports = 0

tech_name = "scn4m_subm"
nominal_corner_only = True

route_supplies = True
check_lvsdrc = True
perimeter_pins = True
#netlist_only = True
#analytical_delay = False
output_name = "sram_{0}rw{1}r{2}w_{3}_{4}_{5}".format(num_rw_ports,
                                                      num_r_ports,
                                                      num_w_ports,
                                                      word_size,
                                                      num_words,
                                                      tech_name)
output_path = "macro/{}".format(output_name)
