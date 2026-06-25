public class Logger{


    private Logger(){
        
        System.out.println("System logger initialized");

    }

    public void log(String message){
        System.out.println("[Log]: "+message);
    }
}