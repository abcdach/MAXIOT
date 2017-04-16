
#include "i2c.h"
#include "ADS1115.h"




bool ICACHE_FLASH_ATTR ADS1115_Init()
{
	//#-----------------------------------------

	//#-----------------------------------------
		uint8 MSB_Config = ADS1115_OS | ADS1115_MUX | ADS1115_PGA | ADS1115_MODE ;
		uint8 LSB_Config = ADS1115_DR | ADS1115_COMP_MODE | ADS1115_COMP_POL | ADS1115_COMP_LAT | ADS1115_COMP_QUE ;
	//#-----------------------------------------
		i2c_start();
		i2c_writeByte(ADS1115_ADDRESS);
		if (!i2c_check_ack()) {
			i2c_stop();
			return(0);
		}
		i2c_writeByte(1);
		if (!i2c_check_ack()) {
			i2c_stop();
			return(0);
		}
		i2c_writeByte(MSB_Config);
		if (!i2c_check_ack()) {
			i2c_stop();
			return(0);
		}
		i2c_writeByte(LSB_Config);
		if (!i2c_check_ack()) {
			i2c_stop();
			return(0);
		}
		i2c_stop();
	//#-----------------------------------------
		return(1);
}


int16_t ICACHE_FLASH_ATTR ADS1115_GetVal( void )
{
	//#-----------------------------------------
		i2c_start();
		i2c_writeByte(ADS1115_ADDRESS);
		if (!i2c_check_ack()) {
			i2c_stop();
			return(0);
		}
		i2c_writeByte(0);
		if (!i2c_check_ack()) {
			i2c_stop();
			return(0);
		}
		i2c_stop();
	//#-----------------------------------------
		os_delay_us(5000);
		//os_delay_us(65000);
	//#-----------------------------------------
		uint8 ack = 0;
		while (!ack) {
			i2c_start();
			i2c_writeByte(ADS1115_ADDRESS+1);
			ack = i2c_check_ack();
			if (!ack) i2c_stop();
		}
		uint8 MSB = i2c_readByte();i2c_send_ack(1);
		uint8 LSB = i2c_readByte();i2c_send_ack(0);
		i2c_stop();
	//#-----------------------------------------
		uint16_t Velue = MSB << 8;
		Velue += LSB;
	//#-----------------------------------------
		//uint16_t Velue2=0;
		if (Velue > 32767){
			Velue = 0;
		}

		//sprintf(ADS1115_Value,"%d",Velue);



	  return Velue;
}




