%Publishes ToF measurements to ROS from a single ToF chip streaming over
%serial

plotReadings = false;
maxWindow = 50;

disp('Booting ROS ToF Node, Ensure serial is running');

%Connect to serial, use seriallist to get all available ports
s = serial('/dev/ttyUSB1');
set(s, 'Timeout', 200);

fopen(s);

%Connect to ROS
try
    rosinit
catch
end

if(plotReadings)
    figure();
    reads = [];
end

%Create ROS topic
tofPub = rospublisher('/tof','std_msgs/Float64');
tofTime = rospublisher('/tofTimes','std_msgs/Time');

while(true)
    %Read serial
    A = fscanf(s);
    A = str2num(A);
    A = double(A);
    
    disp(A);
    
    if(plotReadings)
        reads = [reads; A];
        if(size(reads,1)>maxWindow)
            plot(reads(end-maxWindow:end));
            hold on
            plot(movmean(reads(end-maxWindow:end),4),'--');
            hold off
        else
            plot(reads);
            hold on
            plot(movmean(reads,4));
            hold off
        end
        
        drawnow;
    end
    
    %Publish msg
    msg = rosmessage(tofPub);
    timeMsg = rosmessage(tofTime);
    msg.Data = A;
    timeMsg.Data = rostime('now');
    send(tofPub,msg);
    send(tofTime,timeMsg);
end
