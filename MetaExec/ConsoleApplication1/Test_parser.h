#pragma once
#include "Test.h"
#include "Parser.h"

class TestParser_testOfTests : public SingleTestBase
{
public:
	virtual TestRes Run() override
	{
		return TestRes(EnumTestRes::ok, "Tests working");
	};
};

class TestParser : public TestBase
{
public:
	virtual ~TestParser() = default;
	virtual void prepareAll() override		
	{
		addName("Parser");
		addTest(new TestParser_testOfTests());
	}
};