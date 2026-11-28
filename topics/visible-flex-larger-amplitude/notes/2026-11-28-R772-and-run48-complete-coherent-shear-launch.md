# R772与48 — 厚闭同向参考及真全域剪切求解

会话 Astra-larger-e4e2a2bf-20261126。[R772完整证明](../results/R772-coherent-developed-caps-and-thick-inward-translation-tube.md)，[完整物理生成器](../scripts/resume_20261126/r772_coherent_developing_tube.py)，[48全部完整源/参数/入口交付](../computations/run48-complete-coherent-shear-source-and-launch-delivery.json)。这是新的一个初始闭球和固定g，不借R757/R767/R764的不同g结论。

## 参考已付的全局数学

真单位长轴段、圆角半径.27/四直边各.14的完整闭截圈、两端半径.09的原平滑完整quarter heads及两个真平面全disk构成同一个C²闭球。初相amplitude .01，末1.67；真实中心线用完整R767归一clock积分。参考coherent形为(CX,A,CZ+Z)，整环刚移；整个中带gxx=gee=1，唯一欠价为(sin qt−sin q0)C'_Z的真实混合项。两完整发展盘跨中带/两全头/真正终盘矩形，连同全部真实头和终盘，三Gram准确；不把局部平片扩写成整个闭球准确。

ROOT已完整审读14731B证明、4692B源，特别核全法管链：全时主曲率<21且相对phase中心严格外支撑>1/21；每个|z|<1/21平行面正则、径向投影局部微分同胚，由紧覆盖及S²单连通而全局单射；固定径向线上R'_z=1/(u·N)>0分离不同offset，给整个signed normal map单射，故reach≥1/21。D0<1.55，固定有内点的整右头握径>.68，整像无对齐held>.315，所有t reach>.03D0。原体积−末体积>.11；末面积<3.85及同法管外偏体积界排除任何含反射的E3对齐d<.019，故δE≥.019>.012D0。这些都是此参考场的完整几何界，**没有支付余混合度量**。

另一个normal-offset comparator采用不同初g；其角弦>.60却原角长<.434的障碍不能借给coherent场。单独重标整截圈无法偿混合项，后续R773还排除刚性横环/平行平面环/平移分离类。48必须实际改变物理截圈。

## 48真实自由度和全预算

原六完整初点：coherent族(0,0,0)、(0,.8,.2)、(.04,.5,−1.35)，director族(1,0,0)、(.19,.25,.75)、(.075,.75,−.55)。三参数为真实截圈director转动、真实跨圈料标与真实轴向滑移。修正另外有全world/rim/周期tube/四corner字典的三个Cartesian分量；所有图用同一初始物理位置/材料函数求六jet，真实右头开区保持，左全头和帽可共同移动。时间为同一cubic共同场，全部正结与半结进入法方程；没有对正负端分开拼一个不一致表面。

裸director=(1,0,0)虽使混合/环度量准确，可能甚至必然在末相中站失浸入：x=.5处q=q0=0，轴向列为(0,1−η'Cz,0)，η'=−3π(1.66)sin(t)/.94。末相1/η'落入真实两竖直边Cz∈[−.07,.07]，出现秩降。这个严格裸种子范围不跳过任何一条既定完整训练；三向纠正是否恢复浸入/全g须看真实输出。

六粗点各(24×14,2时间区间,order8,5步)，独立33×19/order12/7相。各族独立赢家完整4/8/16区间：28×20/order10/7步→37×25/order14/17相；38×28/order12/8步→49×35/order16/33相；50×38/order16/9步→65×47/order20/65相。总12完整阶段，两最终点在同runner分别65验证相加七指定整mesh时刻，取并集后均逐相返回、七PLY.GZ真实闭三角网。没有减少相位/空间/变量/迭代/求积。CG160、rtol.0002、damping.0015、jacchunk48、九原线搜；每次实际世界移动上限.033/切向.20；实际area floor.7、权2.5，主曲率bound20、权.018，和三Gram一起进入目标。

终段是R772真实单头/两全盘atlas，不误套R767的.66 bridge缝。实际cylinder/head、head/normal、normal到polar两变量拉回、polar到Cartesian两变量六jet都核；normal宽0/.003/.01，polar半径.25/.875/1，两个真pole均由Cartesian图覆盖。保全relative Gram算子、每个坐标11/12/22独立sup、双向曲率、面积、全对点有序法球弦、整像有限held下界、直径、体积、可能三角接触和全缝；有限测量不是严格全时证书。14整mesh和raw状态留runner，完整public逻辑索引保whole identities。

## 独立根审与每次pull记录

ROOT读四新科学文件、全参数、全部终段、workflow和完整18KB独立监控器，核12实际科学输入与3个旧公共git控制父。新监控器是完整独立文件，旧活run未改。发现旧observer在没有新标量时只在内存更新45min规则pull commit；无法把未知较晚pull冒填旧44/45的H。48现改为每45min即使无新科学标量也完整发布note和H；每次真正checked_pull的时间/commit（含NFF重试中的各次）记在该次完整note，H指其最后真实commit，原科学报告和所有预算未变。容量不足只等整份发布；NFF立即普通pull/rebase再推。

实际源冻结为触发GITHUB_SHA的12完整输入；Python3.12.14、NumPy2.3.5、SciPy1.17.0，360min公共4CPU/16GB，无额外子进程时限/准入。全部9新交付件含完整manifest，科学与参数的原三身份逐一核同；新增规则发布仅控制层。正常触发前未来run/PID/新点/所有数值仍未观测，request.actual全null。参考的reach/held/δE不能传给修正后的实际点；完整同g、后相管及真正精化仍持续欠账。
