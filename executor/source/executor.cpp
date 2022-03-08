#include <iostream>
#include <deque>
#include <array>
#include <memory>

namespace CLR
{
	enum class command
	{
		NOP = 0,
		math_plus  = 0x10,
		math_minus = 0x11,
		math_mult = 0x12,
		math_divide = 0x13,
		math_mod = 0x14
	};
	class StackData
	{
	public:
		long int data;
	};
	class HeapData
	{
	public:

	};
	class Data
	{
	public:
		
		Data() 
		{

		}
		~Data()
		{

		}	
	};
	class Command
	{
	public:
		command commandType;
		Data data;
	};
	class Executor
	{
		std::deque<Command> Commands;
	public:
		Executor()
		{

		}
	};
}

int main()
{
	std::cout << "Hello world" << std::endl;
	return 0;
}