#pragma once
#include <string>
#include <vector>
#include <iostream>

using std::string;
using std::vector;
using std::cout;
using std::endl;

enum class EnumTestRes
{
	ok = 0,
	warn = 1,
	error = 2
};

class TestRes
{
public:
	TestRes(EnumTestRes enumRes, string message) : m_enumRes(enumRes), m_message(message)
	{

	};
	EnumTestRes m_enumRes;
	string m_message;
};

class SingleTestBase
{
public:
	SingleTestBase() = default;
	~SingleTestBase() = default;
	virtual TestRes Run() = 0;
};

class TestBase
{
	vector<SingleTestBase*> m_tests;
	string m_name;
public:	
	~TestBase()
	{
		
	};
	void addTest(SingleTestBase* test)
	{
		m_tests.push_back(test);
	};
	void addName(string name)
	{
		m_name = name;
	}
	virtual void prepareAll() = 0;
	virtual void testAll()
	{
		prepareAll();
		baseTestAll();
		freeAll();
	};
	void baseTestAll()
	{
		cout << "Test of: " << m_name << endl;
		int countAll = m_tests.size();
		int curr = 0;

		if (countAll == 0)
		{
			cout << "No tests added" << endl;
		}
		for (SingleTestBase* pTest : m_tests)
		{
			TestRes res(EnumTestRes::error, "No test");
			if (pTest)
				res = pTest->Run();
			else
			{
				cout << "pTest is null!" << endl;
				return;
			}
			string resToText;
			switch(res.m_enumRes)
			{
				case EnumTestRes::ok:
					resToText = "Passed.";
					break;
				case EnumTestRes::warn:
					resToText = "Warning.";
					break;
				case EnumTestRes::error:
					resToText = "Error.";
					break;
			}
			
			string message;
			if (res.m_message != "")
				message = " message: " + res.m_message;
			
			cout << curr + 1 << "/" << countAll << " " << resToText << message  << endl;
			curr++;
		}
	}
	virtual void freeAll()
	{
		for (SingleTestBase* test : m_tests)
		{
			if (test)
			{
				delete test;
				test = nullptr;
			}
		}
	}
};