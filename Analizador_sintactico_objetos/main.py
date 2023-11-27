import lenguaje
from pila import Pila
from lenguajeEP import EP

pila = Pila()

matriz =    [[	-1	,	-1	,	-1	,	-1	,	5	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-4	,	1	,	2	,	3	,	4	,	-1	,	6	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-2	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-3	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	5	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-4	,	-1	,	7	,	3	,	4	,	-1	,	6	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-6	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-6	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	8	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-7	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-7	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-5	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-9	,	10	,	11	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	9	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	12	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	13	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	15	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-12	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	14	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-8	,	-1	,	-1	,	-1	,	-8	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-8	,	-1	,	-8	,	-8	,	-8	,	-1	,	-8	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-9	,	10	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	16	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	17	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	18	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-10	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	20	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	19	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	22	,	-1	,	-14	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	21	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-11	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-11	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	27	,	-1	,	-1	,	-1	,	5	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-17	,	-1	,	28	,	29	,	30	,	-1	,	-1	,	-1	,	-1	,	-1	,	25	,	-1	,	-1	,	-1	,	-1	,	-1	,	23	,	24	,	-1	,	26	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	31	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-13	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	32	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	33	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	27	,	-1	,	-1	,	-1	,	5	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-17	,	-1	,	28	,	29	,	30	,	-1	,	-1	,	-1	,	-1	,	-1	,	25	,	-1	,	-1	,	-1	,	-1	,	-1	,	34	,	24	,	-1	,	26	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	31	,	-1	,	-1	],
            [	-19	,	-1	,	-1	,	-1	,	-19	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-19	,	-1	,	-19	,	-19	,	-19	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-20	,	-1	,	-1	,	-1	,	-20	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-20	,	-1	,	-20	,	-20	,	-20	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	36	,	-1	,	-1	,	-1	,	35	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	37	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	38	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	46	,	47	,	48	,	49	,	-1	,	42	,	-1	,	-1	,	-1	,	-1	,	43	,	-1	,	-31	,	-1	,	41	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	39	,	-1	,	-1	,	44	,	45	,	-1	,	40	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	50	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	51	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-16	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-16	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-18	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	46	,	47	,	48	,	49	,	-1	,	42	,	-1	,	-1	,	-1	,	-1	,	43	,	-1	,	-1	,	-1	,	41	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	44	,	45	,	-1	,	52	],
            [	46	,	47	,	48	,	49	,	-1	,	42	,	-1	,	-1	,	-1	,	-1	,	43	,	-1	,	-1	,	-1	,	41	,	-33	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	53	,	-1	,	44	,	45	,	-1	,	54	],
            [	46	,	47	,	48	,	49	,	-1	,	42	,	-1	,	-1	,	-1	,	-1	,	43	,	-1	,	-1	,	-1	,	41	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	44	,	45	,	-1	,	55	],
            [	46	,	47	,	48	,	49	,	-1	,	42	,	-1	,	-1	,	-1	,	-1	,	43	,	-1	,	-1	,	-1	,	41	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	44	,	45	,	-1	,	56	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	57	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	59	,	58	,	60	,	63	,	62	,	-1	,	61	,	-32	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	46	,	47	,	48	,	49	,	-1	,	42	,	-1	,	-1	,	-1	,	-1	,	43	,	-1	,	-1	,	-1	,	41	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	44	,	45	,	-1	,	64	],
            [	46	,	47	,	48	,	49	,	-1	,	42	,	-1	,	-1	,	-1	,	-1	,	43	,	-1	,	-1	,	-1	,	41	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	44	,	45	,	-1	,	65	],
            [	46	,	47	,	48	,	49	,	-1	,	42	,	-1	,	-1	,	-1	,	-1	,	43	,	-1	,	-1	,	-1	,	41	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	44	,	45	,	-1	,	66	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-54	,	-54	,	-54	,	-54	,	-54	,	-1	,	-54	,	-54	,	-54	,	-1	,	-54	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-37	,	-37	,	-37	,	-37	,	-37	,	-1	,	-37	,	-37	,	-37	,	-1	,	-37	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-38	,	-38	,	-38	,	-38	,	-38	,	-1	,	-38	,	-38	,	-38	,	36	,	-38	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-39	,	-39	,	-39	,	-39	,	-39	,	-1	,	-39	,	-39	,	-39	,	-1	,	-39	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-40	,	-40	,	-40	,	-40	,	-40	,	-1	,	-40	,	-40	,	-40	,	-1	,	-40	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-41	,	-41	,	-41	,	-41	,	-41	,	-1	,	-41	,	-41	,	-41	,	-1	,	-41	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-27	,	-1	,	-1	,	-1	,	-27	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-27	,	-1	,	-27	,	-27	,	-27	,	-27	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	22	,	-1	,	-14	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	67	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	59	,	58	,	60	,	63	,	62	,	-1	,	61	,	68	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	69	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	59	,	58	,	60	,	63	,	62	,	-1	,	61	,	-1	,	71	,	-1	,	-35	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	70	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	59	,	58	,	60	,	63	,	62	,	-1	,	61	,	-1	,	-1	,	-1	,	72	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	59	,	58	,	60	,	63	,	62	,	-1	,	61	,	-1	,	-1	,	-1	,	73	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-26	,	-1	,	-1	,	-1	,	-26	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-26	,	-1	,	-26	,	-26	,	-26	,	-26	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	46	,	47	,	48	,	49	,	-1	,	42	,	-1	,	-1	,	-1	,	-1	,	43	,	-1	,	-1	,	-1	,	41	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	44	,	45	,	-1	,	74	],
            [	46	,	47	,	48	,	49	,	-1	,	42	,	-1	,	-1	,	-1	,	-1	,	43	,	-1	,	-1	,	-1	,	41	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	44	,	45	,	-1	,	75	],
            [	46	,	47	,	48	,	49	,	-1	,	42	,	-1	,	-1	,	-1	,	-1	,	43	,	-1	,	-1	,	-1	,	41	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	44	,	45	,	-1	,	76	],
            [	46	,	47	,	48	,	49	,	-1	,	42	,	-1	,	-1	,	-1	,	-1	,	43	,	-1	,	-1	,	-1	,	41	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	44	,	45	,	-1	,	77	],
            [	46	,	47	,	48	,	49	,	-1	,	42	,	-1	,	-1	,	-1	,	-1	,	43	,	-1	,	-1	,	-1	,	41	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	44	,	45	,	-1	,	78	],
            [	46	,	47	,	48	,	49	,	-1	,	42	,	-1	,	-1	,	-1	,	-1	,	43	,	-1	,	-1	,	-1	,	41	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	44	,	45	,	-1	,	79	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	59	,	58	,	60	,	63	,	62	,	-1	,	61	,	-1	,	-1	,	-1	,	80	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-46	,	-46	,	-46	,	-46	,	-46	,	-1	,	-46	,	-46	,	-46	,	-1	,	-46	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-47	,	-47	,	-47	,	-47	,	-47	,	-1	,	-47	,	-47	,	-47	,	-1	,	-47	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-15	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-23	,	-1	,	-1	,	-1	,	-23	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-23	,	-1	,	-23	,	-23	,	-23	,	-23	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-42	,	-42	,	-42	,	-42	,	-42	,	-1	,	-42	,	-42	,	-42	,	-1	,	-42	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-34	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	46	,	47	,	48	,	49	,	-1	,	42	,	-1	,	-1	,	-1	,	-1	,	43	,	-1	,	-1	,	-1	,	41	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	44	,	45	,	-1	,	81	],
            [	27	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	85	,	-1	,	-1	,	28	,	29	,	30	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	83	,	-1	,	84	,	-1	,	-1	,	-1	,	-1	,	31	,	82	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	85	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	86	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-48	,	-48	,	-48	,	-48	,	-48	,	-1	,	-48	,	-48	,	-48	,	-1	,	-48	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-49	,	58	,	-49	,	-49	,	-49	,	-1	,	-49	,	-49	,	-49	,	-1	,	-49	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	59	,	58	,	-50	,	-50	,	-50	,	-1	,	-50	,	-50	,	-50	,	-1	,	-50	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	59	,	58	,	60	,	-51	,	-51	,	-1	,	-51	,	-51	,	-51	,	-1	,	-51	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	59	,	58	,	60	,	-52	,	-52	,	-1	,	61	,	-52	,	-52	,	-1	,	-52	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	59	,	58	,	60	,	-53	,	62	,	-1	,	61	,	-53	,	-53	,	-1	,	-53	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-45	,	-45	,	-45	,	-45	,	-45	,	-1	,	-45	,	-45	,	-45	,	-1	,	-45	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	59	,	58	,	60	,	63	,	62	,	-1	,	61	,	-1	,	71	,	-1	,	-35	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	87	,	-1	,	-1	,	-1	,	-1	],
            [	-28	,	-1	,	-1	,	-1	,	-28	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-28	,	-1	,	-28	,	-28	,	-28	,	89	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	88	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-43	,	-1	,	-1	,	-1	,	-43	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-43	,	-1	,	-43	,	-43	,	-43	,	-43	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-44	,	-1	,	-1	,	-1	,	-44	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-44	,	-1	,	-44	,	-44	,	-44	,	-44	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	27	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-21	,	-1	,	28	,	29	,	30	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	90	,	91	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	31	,	-1	,	-1	],
            [	-25	,	-1	,	-1	,	-1	,	-25	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-25	,	-1	,	-25	,	-25	,	-25	,	-25	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-36	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-24	,	-1	,	-1	,	-1	,	-24	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-24	,	-1	,	-24	,	-24	,	-24	,	-24	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	27	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	85	,	-1	,	-1	,	28	,	29	,	30	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	83	,	-1	,	84	,	-1	,	-1	,	-1	,	-1	,	31	,	92	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	93	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	27	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-21	,	-1	,	28	,	29	,	30	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	94	,	91	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	31	,	-1	,	-1	],
            [	-29	,	-1	,	-1	,	-1	,	-29	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-29	,	-1	,	-29	,	-29	,	-29	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-30	,	-1	,	-1	,	-1	,	-30	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-30	,	-1	,	-30	,	-30	,	-30	,	-30	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-22	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	],
            [	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	,	-1	]]


estado = 0
texto = input("Introduce el texto a analizar: ")
elementos = lenguaje.analizador(texto)
e = False
accepted = False
pila.push(0)
a = 0

while(not accepted):
    print(pila)
    input()
    estado = pila.top()##Primer elemento matriz

    #########Segundo elemento matriz########## 
    if elementos[a]['token'] == "id":
        recibido = 0
    elif elementos[a]['token'] == "constante":
        recibido = 1
    elif elementos[a]['token'] == "constante":
        recibido = 2
    elif elementos[a]['token'] == "cadena":
        recibido = 3
    elif elementos[a]['token'] == "Tipo de dato":
        recibido = 4
    elif elementos[a]['token'] == "OpSuma":
        recibido = 5
    elif elementos[a]['token'] == "OpMul":
        recibido = 6
    elif elementos[a]['token'] == "OpRelacional":
        recibido = 7
    elif elementos[a]['token'] == "OpLogico":
        recibido = 8
    elif elementos[a]['token'] == "OpLogico":
        recibido = 9
    elif elementos[a]['token'] == "OpRelacional":
        recibido = 10
    elif elementos[a]['token'] == "OpRelacional":
        recibido = 11
    elif elementos[a]['token'] == "punto y coma":
        recibido = 12
    elif elementos[a]['token'] == "coma":
        recibido = 13
    elif elementos[a]['token'] == "parentesis izq":
        recibido = 14
    elif elementos[a]['token'] == "parentesis der":
        recibido = 15
    elif elementos[a]['token'] == "llave izq":
        recibido = 16
    elif elementos[a]['token'] == "llave der":
        recibido = 17
    elif elementos[a]['token'] == "asignación":
        recibido = 18
    elif elementos[a]['token'] == "condicional SI":
        recibido = 19
    elif elementos[a]['token'] == "While":
        recibido = 20
    elif elementos[a]['token'] == "Return":
        recibido = 21
    elif elementos[a]['token'] == "Else":
        recibido = 22
    elif elementos[a]['token'] == "pesos":
        recibido = 23
    if isinstance(estado, EP):
        if estado.name == "Programa":
            recibido = 24
        elif estado.name == "Definiciones":
            recibido = 25 
        elif estado.name == "Definicion":
            recibido = 26
        elif estado.name == "DefVar":
            recibido = 27
        elif estado.name == "ListaVar":
            recibido = 28
        elif estado.name == "DefFunc":
            recibido = 29
        elif estado.name == "Parametros":
            recibido = 30
        elif estado.name == "ListaParam":
            recibido = 31
        elif estado.name == "BloqFunc":
            recibido = 32
        elif estado.name == "DefLocales":
            recibido = 33
        elif estado.name == "DefLocal":
            recibido = 34
        elif estado.name == "Sentencias":
            recibido = 35
        elif estado.name == "Sentencia":
            recibido = 36
        elif estado.name == "Otro":
            recibido = 37
        elif estado.name == "Bloque":
            recibido = 38
        elif estado.name == "ValorRegresa":
            recibido = 39
        elif estado.name == "Argumentos":
            recibido = 40
        elif estado.name == "ListaArgumentos":
            recibido = 41
        elif estado.name == "Termino":
            recibido = 42
        elif estado.name == "LlamadaFunc":
            recibido = 43
        elif estado.name == "SentenciaBloque":
            recibido = 44
        elif estado.name == "Expresion":
            recibido = 45
        e_cont = pila.pop()
        e = True
        estado = pila.top()
    ##########################################

    accion = matriz[estado][recibido]
    
    if accion == -1:    ####ERROR EN LA CADENA
        print("Cadena no aceptada")
        accepted = True
    elif e:             ####SE RECIBE UN ELEMENTO PILA COMO TOPE POR LO QUE NO HAY DESPLAZAMIENTO
        pila.push(e_cont)
        pila.push(accion)
        e = False
    elif accion >= 0:   ####DESPLAZAMIENTO NORMAL
        pila.push(elementos[a]['lexema'])
        pila.push(accion)
        a+=1

    ####REGLAS####
    elif accion == -2:  ####R0
        print("Cadena aceptada")
        pila.pop()
        b = pila.pop()
        print(b)
        accepted = True
    elif accion == -3:  ####R1
        c = EP("Programa")
        pila.pop()#num
        c.Definiciones = pila.pop()#element
        pila.push(c)
    elif accion == -4:  ####R2
        c = EP("Definiciones")
        c.extra = None #element
        pila.push(c)
    elif accion == -5:  ####R3
        c = EP("Definiciones")
        pila.pop()#num
        c.Definiciones = pila.pop()#element
        pila.pop()#num
        c.Definicion = pila.pop()#element
        pila.push(c)
    elif accion == -6:  ####R4
        c = EP("Definicion")
        pila.pop()#num
        c.DefVar = pila.pop()#element
        pila.push(c)
    elif accion == -7:  ####R5
        c = EP("Definicion")
        pila.pop()#num
        c.DefFunc = pila.pop()#element
        pila.push(c)
    elif accion == -8:  ####R6
        c = EP("DefVar")
        pila.pop()#num
        c.puntoycoma = pila.pop()#element
        pila.pop()#num
        c.ListaVar = pila.pop()#element
        pila.pop()#num
        c.identificador = pila.pop()#element
        pila.pop()#num
        c.tipo = pila.pop()#element
        pila.push(c)
    elif accion == -9:  ####R7
        c = EP("ListaVar")
        c.extra = None #element
        pila.push(c)
    elif accion == -10:  ####R8
        c = EP("ListaVar")
        pila.pop()#num
        c.ListaVar = pila.pop()#element
        pila.pop()#num
        c.identificador = pila.pop()#element
        pila.pop()#num
        c.coma = pila.pop()#element
        pila.push(c)
    elif accion == -11:  ####R9
        c = EP("DefFunc")
        pila.pop()#num
        c.BloqFunc = pila.pop()#element
        pila.pop()#num
        c.parentesiscerrar = pila.pop()#element
        pila.pop()#num
        c.Parametros = pila.pop()#element
        pila.pop()#num
        c.parentesisabrir = pila.pop()#element
        pila.pop()#num
        c.identificador = pila.pop()#element
        pila.pop()#num
        c.tipo = pila.pop()#element
        pila.push(c)
    elif accion == -12:  ####R10
        c = EP("Parametros")
        c.extra = None #element
        pila.push(c)
    elif accion == -13:  ####R11
        c = EP("Parametros")
        pila.pop()#num
        c.ListaParam = pila.pop()#element
        pila.pop()#num
        c.identificador = pila.pop()#element
        pila.pop()#num
        c.tipo = pila.pop()#element
        pila.push(c)
    elif accion == -14:  ####R12
        c = EP("ListaParam")
        c.extra = None #element
        pila.push(c)
    elif accion == -15:  ####R13
        c = EP("ListaParam")
        pila.pop()#num
        c.ListaParam = pila.pop()#element
        pila.pop()#num
        c.identificador = pila.pop()#element
        pila.pop()#num
        c.tipo = pila.pop()#element
        pila.pop()#num
        c.coma = pila.pop()#element
        pila.push(c)
    elif accion == -16:  ####R14
        c = EP("BloqFunc")
        pila.pop()#num
        c.llavecerrar = pila.pop()#element
        pila.pop()#num
        c.DefLocales = pila.pop()#element
        pila.pop()#num
        c.llaveabrir = pila.pop()#element
        pila.push(c)
    elif accion == -17:  ####R15
        c = EP("DefLocales")
        c.extra = None #element
        pila.push(c)
    elif accion == -18:  ####R16
        c = EP("DefLocales")
        pila.pop()#num
        c.DefLocales = pila.pop()#element
        pila.pop()#num
        c.DefLocal = pila.pop()#element
        pila.push(c)
    elif accion == -19:  ####R17
        c = EP("DefLocal")
        pila.pop()#num
        c.DefVar = pila.pop()#element
        pila.push(c)
    elif accion == -20:  ####R18
        c = EP("DefLocal")
        pila.pop()#num
        c.Sentencia = pila.pop()#element
        pila.push(c)
    elif accion == -21:  ####R19
        c = EP("Sentencias")
        c.extra = None #element
        pila.push(c)
    elif accion == -22:  ####R20
        c = EP("Sentencias")
        pila.pop()#num
        c.Sentencias = pila.pop()#element
        pila.pop()#num
        c.Sentencia = pila.pop()#element
        pila.push(c)
    elif accion == -23:  ####R21
        c = EP("Sentencia")
        pila.pop()#num
        c.puntoycoma = pila.pop()#element
        pila.pop()#num
        c.Expresion = pila.pop()#element
        pila.pop()#num
        c.igual = pila.pop()#element
        pila.pop()#num
        c.identificador = pila.pop()#element
        pila.push(c)
    elif accion == -24:  ####R22
        c = EP("Sentencia")
        pila.pop()#num
        c.Otro = pila.pop()#element
        pila.pop()#num
        c.SentenciaBloque = pila.pop()#element
        pila.pop()#num
        c.parentesiscerrar = pila.pop()#element
        pila.pop()#num
        c.Expresion = pila.pop()#element
        pila.pop()#num
        c.parentesisabrir = pila.pop()#element
        pila.pop()#num
        c.palabraif = pila.pop()#element
        pila.push(c)
    elif accion == -25:  ####R23
        c = EP("Sentencia")
        pila.pop()#num
        c.Bloque = pila.pop()#element
        pila.pop()#num
        c.parentesiscerrar = pila.pop()#element
        pila.pop()#num
        c.Expresion = pila.pop()#element
        pila.pop()#num
        c.parentesisabrir = pila.pop()#element
        pila.pop()#num
        c.palabrawhile = pila.pop()#element
        pila.push(c)
    elif accion == -26:  ####R24
        c = EP("Sentencia")
        pila.pop()#num
        c.puntoycoma = pila.pop()#element
        pila.pop()#num
        c.ValorRegresa = pila.pop()#element
        pila.pop()#num
        c.palabrareturn = pila.pop()#element
        pila.push(c)
    elif accion == -27:  ####R25
        c = EP("Sentencia")
        pila.pop()#num
        c.puntoycoma = pila.pop()#element
        pila.pop()#num
        c.LlamadaFunc = pila.pop()#element
        pila.push(c)
    elif accion == -28:  ####R26
        c = EP("Otro")
        c.extra = None #element
        pila.push(c)
    elif accion == -29:  ####R27
        c = EP("Otro")
        pila.pop()#num
        c.SentenciaBloque = pila.pop()#element
        pila.pop()#num
        c.palabraelse = pila.pop()#element
        pila.push(c)
    elif accion == -30:  ####R28
        c = EP("Bloque")
        pila.pop()#num
        c.llavecerrar = pila.pop()#element
        pila.pop()#num
        c.Sentencias = pila.pop()#element
        pila.pop()#num
        c.llaveabrir = pila.pop()#element
        pila.push(c)
    elif accion == -31:  ####R29
        c = EP("ValorRegresa")
        c.extra = None #element
        pila.push(c)
    elif accion == -32:  ####R30
        c = EP("ValorRegresa")
        pila.pop()#num
        c.Expresion = pila.pop()#element
        pila.push(c)
    elif accion == -33:  ####R31
        c = EP("Argumentos")
        c.extra = None #element
        pila.push(c)
    elif accion == -34:  ####R32
        c = EP("Argumentos")
        pila.pop()#num
        c.ListaArgumentos = pila.pop()#element
        pila.pop()#num
        c.Expresion = pila.pop()#element
        pila.push(c)
    elif accion == -35:  ####R33
        c = EP("ListaArgumentos")
        c.extra = None #element
        pila.push(c)
    elif accion == -36:  ####R34
        c = EP("ListaArgumentos")
        pila.pop()#num
        c.ListaArgumentos = pila.pop()#element
        pila.pop()#num
        c.Expresion = pila.pop()#element
        pila.pop()#num
        c.coma = pila.pop()#element
        pila.push(c)
    elif accion == -37:  ####R35
        c = EP("Termino")
        pila.pop()#num
        c.LlamadaFunc = pila.pop()#element
        pila.push(c)
    elif accion == -38:  ####R36
        c = EP("Termino")
        pila.pop()#num
        c.identificador = pila.pop()#element
        pila.push(c)
    elif accion == -39:  ####R37
        c = EP("Termino")
        pila.pop()#num
        c.entero = pila.pop()#element
        pila.push(c)
    elif accion == -40:  ####R38
        c = EP("Termino")
        pila.pop()#num
        c.real = pila.pop()#element
        pila.push(c)
    elif accion == -41:  ####R39
        c = EP("Termino")
        pila.pop()#num
        c.cadena = pila.pop()#element
        pila.push(c)
    elif accion == -42:  ####R40
        c = EP("LlamadaFunc")
        pila.pop()#num
        c.parentesiscerrar = pila.pop()#element
        pila.pop()#num
        c.Argumentos = pila.pop()#element
        pila.pop()#num
        c.parentesisabrir = pila.pop()#element
        pila.pop()#num
        c.identificador = pila.pop()#element
        pila.push(c)
    elif accion == -43:  ####R41
        c = EP("SentenciaBloque")
        pila.pop()#num
        c.Sentencia = pila.pop()#element
        pila.push(c)
    elif accion == -44:  ####R42
        c = EP("SentenciaBloque")
        pila.pop()#num
        c.Bloque = pila.pop()#element
        pila.push(c)
    elif accion == -45:  ####R43
        c = EP("Expresion")
        pila.pop()#num
        c.parentesiscerrar = pila.pop()#element
        pila.pop()#num
        c.Expresion = pila.pop()#element
        pila.pop()#num
        c.parentesisabrir = pila.pop()#element
        pila.push(c)
    elif accion == -46:  ####R44
        c = EP("Expresion")
        pila.pop()#num
        c.Expresion = pila.pop()#element
        pila.pop()#num
        c.opSuma = pila.pop()#element
        pila.push(c)
    elif accion == -47:  ####R45
        c = EP("Expresion")
        pila.pop()#num
        c.Expresion = pila.pop()#element
        pila.pop()#num
        c.opNot = pila.pop()#element
        pila.push(c)
    elif accion == -48:  ####R46
        c = EP("Expresion")
        pila.pop()#num
        c.Expresion = pila.pop()#element
        pila.pop()#num
        c.opMul = pila.pop()#element
        pila.pop()#num
        c.Expresion = pila.pop()#element
        pila.push(c)
    elif accion == -49:  ####R47
        c = EP("Expresion")
        pila.pop()#num
        c.Expresion = pila.pop()#element
        pila.pop()#num
        c.opSuma = pila.pop()#element
        pila.pop()#num
        c.Expresion = pila.pop()#element
        pila.push(c)
    elif accion == -50:  ####R48
        c = EP("Expresion")
        pila.pop()#num
        c.Expresion = pila.pop()#element
        pila.pop()#num
        c.opRelac = pila.pop()#element
        pila.pop()#num
        c.Expresion = pila.pop()#element
        pila.push(c)
    elif accion == -51:  ####R49
        c = EP("Expresion")
        pila.pop()#num
        c.Expresion = pila.pop()#element
        pila.pop()#num
        c.opIgualdad = pila.pop()#element
        pila.pop()#num
        c.Expresion = pila.pop()#element
        pila.push(c)
    elif accion == -52:  ####R50
        c = EP("Expresion")
        pila.pop()#num
        c.Expresion = pila.pop()#element
        pila.pop()#num
        c.opAnd = pila.pop()#element
        pila.pop()#num
        c.Expresion = pila.pop()#element
        pila.push(c)
    elif accion == -53:  ####R51
        c = EP("Expresion")
        pila.pop()#num
        c.Expresion = pila.pop()#element
        pila.pop()#num
        c.opOr = pila.pop()#element
        pila.pop()#num
        c.Expresion = pila.pop()#element
        pila.push(c)
    elif accion == -54:  ####R52
        c = EP("Expresion")
        pila.pop()#num
        c.Termino = pila.pop()#element
        pila.push(c)

    