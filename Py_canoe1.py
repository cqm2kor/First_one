
from py_canoe import CANoe
from time import sleep as wait

canoe_inst = CANoe()
canoe_inst.open(canoe_cfg=r"c:\Users\Public\Documents\Vector\CANoe\Sample Configurations 18.3.118\CAN\CANSystemDemo\CANSystemDemo.cfg")

canoe_inst.start_measurement()
wait(2)

#sys_var_val = canoe_inst.get_system_variable_value('ComfortBus::ShowMultiDisplay')
#print(sys_var_val)
print("Hello World")
#resp = canoe_inst.send_diag_request('Door_Left', '1A 90')
#print(resp)
canoe_inst.stop_measurement()

