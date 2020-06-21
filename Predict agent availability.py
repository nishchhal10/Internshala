import unittest

class LearnTest(unittest.TestCase):
    def test_func_1(self):
        #arrange
        no_of_customer=5
        no_of_agents=2
        start_time=[5,10,15,20,25]
        resolution_time=[11, 11, 5 ,2 ,4]


        #act
        result1 = predict(no_of_customer,no_of_agents,start_time,resolution_time,agent_status)
        #assert
        self.assertEqual(result1,[5, 10, 16, 21, 25])
        pass
    def test_func_2(self):
        no_of_customer = 3
        no_of_agents = 1
        start_time = [5, 10, 15]
        resolution_time = [6,2,10]

        # act
        result1 = predict(no_of_customer,no_of_agents,start_time,resolution_time,agent_status)
        # assert
        self.assertEqual(result1,[5, 11, 15])


def predict(no_of_customer,no_of_agents,start_time,resolution_time,agent_status):

    result = []
    agent_status = [0] * no_of_agents
    for k in range(no_of_agents):
        #print(start_time[k] ,end= " ")
        try:
            result.append(start_time[k])
            agent_status[k] = start_time[k] +resolution_time[k]
        except:
            return (result)
    for i in range(no_of_agents ,no_of_customer):
        sorted(agent_status)
        if (start_time[i] < agent_status[0]):
            #print(agent_status[0], end=" ")
            result.append(agent_status[0])
            agent_status[0] = agent_status[0] + resolution_time[i]
        else:
            #print(start_time[i] ,end =" ")
            result.append(start_time[i])
            agent_status[0] = start_time[i] +resolution_time[i]
    return(result)

#output denotes the timestamp at which agent will start processing the task assigned to him/her

if __name__ == "__main__":
    no_of_customer, no_of_agents = map(int,(input().split()))  # denotes the number of customers and no of agents at work
    start_time = list(map(int, input().split()))  # denotes the timestamp at which the customer enters the office
    resolution_time = list(map(int, input().split()))  # denotes the time which is required to fulfill his/her request.
    agent_status = [0] * no_of_agents  # stores the current status of agent i.e time at which the agent will be free
    print(predict(no_of_customer,no_of_agents,start_time,resolution_time,agent_status))
    unittest.main()
