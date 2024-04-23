#include "supervisor_list.h"
#include "supR0EsteiraSensor.h"
#include "supEsteiraMesa_GiratoriaR1.h"
#include "supR2Mesa_GiratoriaFuradeira.h"
#include "supR3Mesa_GiratoriaTeste.h"
#include "supR4Mesa_GiratoriaRobo.h"
#include "supR5EsteiraMesa_GiratoriaFuradeira.h"
#include "supR6Mesa_GiratoriaFuradeiraTeste.h"
#include "supR7Mesa_GiratoriaTesteRobo.h"
#include "supR8EsteiraMesa_GiratoriaFuradeiraTeste.h"

// make list with all supervisors
// first create all supervisors
extern SupervisorList supR0EsteiraSensor_list;
extern SupervisorList supEsteiraMesa_GiratoriaR1_list;
extern SupervisorList supR2Mesa_GiratoriaFuradeira_list;
extern SupervisorList supR3Mesa_GiratoriaTeste_list;
extern SupervisorList supR4Mesa_GiratoriaRobo_list;
extern SupervisorList supR5EsteiraMesa_GiratoriaFuradeira_list;
extern SupervisorList supR6Mesa_GiratoriaFuradeiraTeste_list;
extern SupervisorList supR7Mesa_GiratoriaTesteRobo_list;
extern SupervisorList supR8EsteiraMesa_GiratoriaFuradeiraTeste_list;

// then recreate and linking them
SupervisorList sup_list = {&supR0EsteiraSensor, &supEsteiraMesa_GiratoriaR1_list};
SupervisorList supEsteiraMesa_GiratoriaR1_list = {&supEsteiraMesa_GiratoriaR1, &supR2Mesa_GiratoriaFuradeira_list};
SupervisorList supR2Mesa_GiratoriaFuradeira_list = {&supR2Mesa_GiratoriaFuradeira, &supR3Mesa_GiratoriaTeste_list};
SupervisorList supR3Mesa_GiratoriaTeste_list = {&supR3Mesa_GiratoriaTeste, &supR4Mesa_GiratoriaRobo_list};
SupervisorList supR4Mesa_GiratoriaRobo_list = {&supR4Mesa_GiratoriaRobo, &supR5EsteiraMesa_GiratoriaFuradeira_list};
SupervisorList supR5EsteiraMesa_GiratoriaFuradeira_list = {&supR5EsteiraMesa_GiratoriaFuradeira, &supR6Mesa_GiratoriaFuradeiraTeste_list};
SupervisorList supR6Mesa_GiratoriaFuradeiraTeste_list = {&supR6Mesa_GiratoriaFuradeiraTeste, &supR7Mesa_GiratoriaTesteRobo_list};
SupervisorList supR7Mesa_GiratoriaTesteRobo_list = {&supR7Mesa_GiratoriaTesteRobo, &supR8EsteiraMesa_GiratoriaFuradeiraTeste_list};
SupervisorList supR8EsteiraMesa_GiratoriaFuradeiraTeste_list = {&supR8EsteiraMesa_GiratoriaFuradeiraTeste, NULL};
