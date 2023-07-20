public class MyProgram extends ConsoleProgram
{
    
    private static final String user_win = "User wins!!";
    private static final String comp_win = "Computer wins!!";
    private static final String tie = "its a Tie!";
    

    private String getWinner(String user, String computer)
    {
        String user_win = "User Wins!!";
        String comp_win = " Computer wins!!";
        String tie = "its a tie!";
        
        if (user.equals("rock"))
        {
            if (computer.equals("paper"))
            {
                return comp_win;
            }
            
            if (computer.equals("scissors"))
            {
                return user_win;
            }
            else
            {
                return tie;
            }
        }
        
        else if (user.equals("paper"))
        {
            if (computer.equals("scissors"))
            {
                return comp_win;
            }
            
            if (computer.equals("rock"))
            {
                return user_win;
            }
            else
            {
                return tie;
            }
        }
        
        else if (user.equals("scissors"))
        {
            if (computer.equals("rock"))
            {
                return comp_win;
            }
            
            if (computer.equals("paper"))
            {
                return user_win;
            }
            else
            {
                return tie;
            }
        }
        
        return "good game!";
    }
    
    public void run()
    {
        Teller();
    }
    
    public void Teller()
    {
            String user_input = readLine(" Enter your choice rock, paper, or scissors: ");
        
        if (user_input.equals(""))
        {
            System.out.println(" Thanks for playing!!");
        }
        else
        {
            int rand = Randomizer.nextInt(1,3);
            String compinput = "";
            if (rand == 1)
            {
                compinput = "rock";
            }
            else if (rand == 2)
            {
                compinput = "paper";    
                
            }
            else
            {
                compinput = "scissors";
            }
            
            System.out.println("User: " + user_input);
            System.out.println("Computer: " + compinput);
            System.out.println(getWinner(user_input,compinput));
            
            
        }
        
        
    }
    
    
    
    
}
