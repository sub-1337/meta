#include <iostream>
#include <deque>
#include <array>
#include <memory>

namespace MetaCLR
{
	enum class enumCommand
	{
		NOP = 0,
		math_plus  = 0x10,
		math_minus = 0x11,
		math_mult = 0x12,
		math_divide = 0x13,
		math_mod = 0x14,

		alloc = 0x100,
		let = 0x200,

		call = 0x1000
	};

	//class StackData
	//{
	//public:
	//	long int data;
	//};

	//class HeapData
	//{
	//public:

	//};

	class Data
	{

	public:
		int d;
		Data()
		{
			d = 0;
		}
		Data(int d) 
		{
			d = d;
		}
		~Data()
		{

		}	
	};

	class Command
	{
	public:
		enumCommand commandType;
		Data data;
	};

	class Code
	{
	public:
		std::deque<Command> Commands;
		void Compile(std::string strCode)
		{
			Command p_a;
			p_a.commandType = enumCommand::alloc;
			Command p_a2;
			p_a2.commandType = enumCommand::let;
			p_a2.data = 2;

			Command p_b;
			p_b.commandType = enumCommand::alloc;
			Command p_b2;
			p_b2.commandType = enumCommand::let;
			p_b2.data = 3;

			Command p_c;
			p_c.commandType = enumCommand::math_plus;

			Command p_print;
			p_print.commandType = enumCommand::call;
			p_print.data = 1;
			Commands.push_front(p_a);
			Commands.push_front(p_a2);
			Commands.push_front(p_b);
			Commands.push_front(p_b2);
			Commands.push_front(p_c);
			Commands.push_front(p_print);
		}
		Command NextCommand()
		{
			Command com = Commands.front();
			Commands.pop_front();
			return com;
		}
		bool IsEmpty()
		{
			return (Commands.size() == true);
		}
		~Code()
		{

		}
	};

	class Executor
	{
		Code currCode;
		void exec(Command currCommand)
		{
			if (currCommand == enumCommand::alloc)
			{

			}
		}
	public:
		Executor()
		{

		}
		void Run()
		{
			while (!currCode.IsEmpty())
			{
				exec(currCode.NextCommand());
			}
		}
		void SetCode(Code code)
		{
			currCode = code;
		}
	};
}

int main()
{	
	MetaCLR::Code code;
	std::string strCode = "a = 2; b = 3; c = a + b; print(c)";
	code.Compile(strCode);

	MetaCLR::Executor exec;
	exec.SetCode(code);

	exec.Run();
	std::cout << "Hello world" << std::endl;
	return 0;
}