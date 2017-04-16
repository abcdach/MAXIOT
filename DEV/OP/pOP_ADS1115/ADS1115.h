#ifndef __I2C_SHT21_H
#define	__I2C_SHT21_H

#include "c_types.h"
//#include "ets_sys.h"
//#include "osapi.h"
#include "gpio.h"
#include "esp_common.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "lwip/sockets.h"
#include "lwip/dns.h"
#include "lwip/netdb.h"

#define ADS1115_ADDRESS 0x90 //0x48*2



//extern uint16_t ADS1115_Value;

bool ICACHE_FLASH_ATTR ADS1115_Init();
int16_t ICACHE_FLASH_ATTR ADS1115_GetVal( void );

//#----------------------------------------------------------------------
//#	Operational status/single-shot conversion start
//#----------------------------------------------------------------------

//	#define ADS1115_OS		0 << 7		//No effect
	#define ADS1115_OS		1 << 7		//Begin a single conversion (when in power-down mode)

//#----------------------------------------------------------------------
//#	Input multiplexer configuration
//#----------------------------------------------------------------------

//	#define ADS1115_MUX		0 << 4		//000 : AINP = AIN0 and AINN = AIN1 -- default
//	#define ADS1115_MUX		1 << 4		//001 : AINP = AIN0 and AINN = AIN3
//	#define ADS1115_MUX		2 << 4		//010 : AINP = AIN1 and AINN = AIN3
	#define ADS1115_MUX		3 << 4		//011 : AINP = AIN2 and AINN = AIN3
//	#define ADS1115_MUX		4 << 4		//100 : AINP = AIN0 and AINN = GND
//	#define ADS1115_MUX		5 << 4		//101 : AINP = AIN1 and AINN = GND
//	#define ADS1115_MUX		6 << 4		//110 : AINP = AIN2 and AINN = GND
//	#define ADS1115_MUX		7 << 4		//111 : AINP = AIN3 and AINN = GND

//#----------------------------------------------------------------------
//#	Programmable gain amplifier configuration
//#----------------------------------------------------------------------
//	#define ADS1115_PGA		0 << 1		//000 : FS = ±6.144V --	This parameter expresses the full-scale range of the ADC scaling. In no event should more than VDD + 0.3V be applied to this device.
	#define ADS1115_PGA		1 << 1		//001 : FS = ±4.096V -- This parameter expresses the full-scale range of the ADC scaling. In no event should more than VDD + 0.3V be applied to this device.
//	#define ADS1115_PGA		2 << 1		//010 : FS = ±2.048V
//	#define ADS1115_PGA		3 << 1		//011 : FS = ±1.024V
//	#define ADS1115_PGA		4 << 1		//100 : FS = ±0.512V
//	#define ADS1115_PGA		5 << 1		//101 : FS = ±0.256V
//	#define ADS1115_PGA		6 << 1		//110 : FS = ±0.256V -- default)
//	#define ADS1115_PGA		7 << 1		//111 : FS = ±0.256V

//#----------------------------------------------------------------------
//#	Device operating mode
//#----------------------------------------------------------------------

	#define ADS1115_MODE		0 << 0		//Continuous conversion mode
//	#define ADS1115_MODE		1 << 0		//Power-down single-shot mode -- default

//#----------------------------------------------------------------------
//#	Data rate
//#----------------------------------------------------------------------

	#define ADS1115_DR		0 << 5		//000 : 8SPS
//	#define ADS1115_DR		1 << 5		//001 : 16SPS
//	#define ADS1115_DR		2 << 5		//010 : 32SPS
//	#define ADS1115_DR		3 << 5		//011 : 64SPS
//	#define ADS1115_DR		4 << 5		//100 : 128SPS -- default
//	#define ADS1115_DR		5 << 5		//101 : 250SPS
//	#define ADS1115_DR		6 << 5		//110 : 475SPS
//	#define ADS1115_DR		7 << 5		//111 : 860SPS

//#----------------------------------------------------------------------
//#	Comparator mode
//#----------------------------------------------------------------------

	#define ADS1115_COMP_MODE		0 << 4		//Traditional comparator with hysteresis -- default
//	#define ADS1115_COMP_MODE		1 << 4		//Window comparator

//#----------------------------------------------------------------------
//#	Comparator polarity
//#----------------------------------------------------------------------

	#define ADS1115_COMP_POL		0 << 3		//Active low -- default
//	#define ADS1115_COMP_POL		1 << 3		//Active high

//#----------------------------------------------------------------------
//#	Latching comparator
//#----------------------------------------------------------------------

	#define ADS1115_COMP_LAT		0 << 2		//Non-latching comparator -- default
//	#define ADS1115_COMP_LAT		1 << 2		//Latching comparator

//#----------------------------------------------------------------------
//#	Comparator queue and disable
//#----------------------------------------------------------------------

//	#define ADS1115_COMP_QUE		0 << 0		//00 : Assert after one conversion
//	#define ADS1115_COMP_QUE		1 << 0		//01 : Assert after two conversions
//	#define ADS1115_COMP_QUE		2 << 0		//10 : Assert after four conversions
	#define ADS1115_COMP_QUE		3 << 0		//11 : Disable comparator (default)



#endif


















