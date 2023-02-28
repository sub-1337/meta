#include <iostream>
#include <deque>
#include <array>
#include <map>
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

	class Data
	{

	public:
		int a;
		int b;
		int c;
		std::string comment;
		Data()
		{
			a = 0;
			b = 0;
			c = 0;
		}
		Data(int a, int b, int c) 
		{
			this->a = a;
			this->b = b;
			this->c = c;
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
			p_a.data.a = 1; // 1st var
			p_a.data.comment = "1st instr";

			Command p_a2;
			p_a2.commandType = enumCommand::let;
			p_a2.data.a = 1; // 1st var
			p_a2.data.b = 2;
			p_a2.data.comment = "2nd instr";

			Command p_b;
			p_b.commandType = enumCommand::alloc;
			p_b.data.a = 2; // 2nd var
			Command p_b2;
			p_b2.commandType = enumCommand::let;
			p_b2.data.a = 2; // 2nd var
			p_b2.data.b = 3;

			Command p_c;
			p_c.commandType = enumCommand::alloc;
			p_c.data.a = 3; // 3rd var

			Command p_c2;
			p_c2.commandType = enumCommand::math_plus;
			p_c2.data.a = 3; // 3st var (result)
			p_c2.data.b = 1; // 1st var
			p_c2.data.c = 2; // 2nd var


			Command p_print;
			p_print.commandType = enumCommand::call;
			p_print.data.a = 1; // function #1
			p_print.data.b = 3; // third var
			p_print.data.comment = "Print call";

			Commands.push_back(p_a);
			Commands.push_back(p_a2);
			Commands.push_back(p_b);
			Commands.push_back(p_b2);
			Commands.push_back(p_c);
			Commands.push_back(p_c2);
			Commands.push_back(p_print);
		}
		Command NextCommand()
		{
			Command com = Commands.front();
			Commands.pop_front();
			return com;
		}
		bool IsEmpty()
		{
			return (Commands.empty());
		}
		~Code()
		{

		}
	};

	class Executor
	{
		Code currCode;
		std::map<int, int> memory;
		//std::map<int, void*> memory_func;
		void exec(Command currCommand)
		{
			if (currCommand.commandType == enumCommand::alloc)
			{
				memory.insert({ currCommand.data.a,0 });
			}
			if (currCommand.commandType == enumCommand::let)
			{
				memory[currCommand.data.a] = currCommand.data.b;
			}
			if (currCommand.commandType == enumCommand::math_plus)
			{
				memory[currCommand.data.a] = memory[currCommand.data.b] + memory[currCommand.data.c];
			}
			if (currCommand.commandType == enumCommand::math_minus)
			{
				memory[currCommand.data.a] = memory[currCommand.data.b] - memory[currCommand.data.c];
			}
			if (currCommand.commandType == enumCommand::math_mod)
			{
				memory[currCommand.data.a] = memory[currCommand.data.b] % memory[currCommand.data.c];
			}
			if (currCommand.commandType == enumCommand::math_mult)
			{
				memory[currCommand.data.a] = memory[currCommand.data.b] * memory[currCommand.data.c];
			}
			if (currCommand.commandType == enumCommand::math_divide)
			{
				memory[currCommand.data.a] = memory[currCommand.data.b] / memory[currCommand.data.c];
			}
			if (currCommand.commandType == enumCommand::call)
			{
				switch (currCommand.data.a)
				{
				case 1:
					std::cout << memory[currCommand.data.b];
				}
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