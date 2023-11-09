#1到38行 ，画地图。
import matplotlib.pyplot as plt
import sys
def readline_count(file_name):

    return len(open(file_name).readlines())
def main(args):
    plt.ion()     #打开交互模式，显示作图过程
    fig=plt.figure()
    f_line=open("map_data/Type_Line.txt",'r',encoding='UTF-8')
    f_bezier=open("map_data/Type_Bezier.txt",'r',encoding='UTF-8')
    f_station = open("map_data/agv_station_gai.txt", 'r', encoding='UTF-8')
    line_data=[]
    bezier_data=[]
    station_data=[]
    for line in f_station:
        b=line.split()
        station_data.append(b)
    for line in f_line:
        b=line.split()
        line_data.append(b)
    for line in f_bezier:
        a=line.split()
        bezier_data.append(a)
    ax = fig.add_subplot(111)
    for i in range(len(station_data)):
        #l=len(line_data[i])
        p_x=float(station_data[i][0])
        p_y=float(station_data[i][1])
        ax.scatter(p_x,p_y,5,'b')
        #ax.text(p_x,p_y,str_list[i][0])  #每个站点的标号
    for i in range(len(bezier_data)):
        p_x=float(bezier_data[i][4])
        p_y=float(bezier_data[i][5])
        x = float(bezier_data[i][6])
        y = float(bezier_data[i][7])
        if bezier_data[8]=="Bothway":
            ax.arrow(p_x, p_y, x - p_x, y - p_y, width=0.03, length_includes_head=True, head_length=0.2, color='green')
            ax.arrow(x,y,p_x-x,p_y-y,width=0.03,length_includes_head=True,head_length=0.2,color='green')
        else:
            ax.arrow(p_x, p_y, x - p_x, y - p_y, width=0.03, length_includes_head=True, head_length=0.2, color='green')
    #print(len(line_data))
    for i in range(len(line_data)):
        p_x=float(line_data[i][0])
        p_y=float(line_data[i][1])
        x = float(line_data[i][2])
        y = float(line_data[i][3])
        if line_data[4]=="Bothway":
            ax.arrow(p_x, p_y, x - p_x, y - p_y, width=0.03, length_includes_head=True, head_length=0.2, color='green')
            ax.arrow(x,y,p_x-x,p_y-y,width=0.03,length_includes_head=True,head_length=0.2,color='green')
        else:
            ax.arrow(p_x, p_y, x - p_x, y - p_y, width=0.03, length_includes_head=True, head_length=0.2, color='green')

    f_p=open(args[0],'r',encoding='UTF-8')
    car_data=[]
    for i in range(int(args[1])):
        car=[]
        for j in  range(120):
            line=f_p.readline()
            if line.startswith('car'):
                break
            a=line.split()
            car.append(a)
        car_data.append(car)
        i+=1

    t=0
    color=['yellow','violet','brown','red','sienna','tan','gold','green','cyan','dodgerblue']#第几量小车用第几个颜色
    for m in range(500):        #每隔一段时间确定小车位置
        for i in range(len(car_data)):   #对每辆小车循环(i代表第几量小车)
            for j in range(len(car_data[i])):
                #print(car_data[1][j][1])
                a=(car_data[i][j][1]).split('->')     #小车第二个数据（时间A——>时间B）
                #print(a[0],a[1])  #(正常)
                str_time=float(a[0])
                end_time=float(a[1])
                if t>=str_time and t<=end_time:
                    b=(car_data[i][j][0]).split('->')  #提取每行第一个数据（坐标名）  索引号
                    x1=float(station_data[int(b[0])][0])
                    y1=float(station_data[int(b[0])][1])
                    #print(x1,y1)
                    x2 = float(station_data[int(b[1])][0])
                    y2 = float(station_data[int(b[1])][1])
                    consum = float(car_data[i][j][2])    #此段路消耗时间
                    bi = (t - str_time) / consum        #当前时间减去上个在站点的时间，再比上此段路所需的全部时间   #小车竖着走
                    addy=(y2-y1)*bi
                    addx=(x2-x1)*bi
                    ax.scatter(x1+addx,y1+addy,5,color[i])
                    break
        t+=float(args[2])
        plt.pause(0.1)  #每隔一秒显示计算一次
    plt.ioff()
    f_line.close()
    f_line.close()
    f_station.close()
    f_p.close()
    plt.show()
if __name__=="__main__":
    args=sys.argv[1:]
    main(args)
