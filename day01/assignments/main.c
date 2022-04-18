/*
 *By Alain Thierry, 04/2022
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char const *argv[])
{
	
	double cpu_time;
	double bandwidth = 0.0;
	int SAMPLE = 60000000;
	int stride = 20;
	int MAX_LENGTH = (SAMPLE)*stride;
	int *ARRAY = malloc(MAX_LENGTH*sizeof(double));
	float mean = 0;
	double cpu_time_msec = 0.0;

	for (int i = 0; i < MAX_LENGTH; ++i)
	{
		ARRAY[i] = rand() + i/2;
	}
	printf("STIDE CPU TIME(ms) BANDWIDTH (MB/s) \n");
	for (int i_stride = 1; i_stride <= stride; i_stride++)
	{
		clock_t start_time = clock();	// Start taking time of concerned part
		for (int i = 1; i <= SAMPLE*i_stride; i+=i_stride)
		{
			mean +=ARRAY[i-1];
		}
		clock_t end_time = clock();		// End time 
		
		cpu_time = ((double) (end_time - start_time))/CLOCKS_PER_SEC; //In seconds
		bandwidth = sizeof(double) * SAMPLE * (cpu_time) / (1024*1024); 
		cpu_time_msec = cpu_time*1000.0;	// convert cpu time into millisecond
		printf("%d , %f, %f \n", i_stride, cpu_time_msec, bandwidth);
	} 
	free(ARRAY);
	return 0;
}
