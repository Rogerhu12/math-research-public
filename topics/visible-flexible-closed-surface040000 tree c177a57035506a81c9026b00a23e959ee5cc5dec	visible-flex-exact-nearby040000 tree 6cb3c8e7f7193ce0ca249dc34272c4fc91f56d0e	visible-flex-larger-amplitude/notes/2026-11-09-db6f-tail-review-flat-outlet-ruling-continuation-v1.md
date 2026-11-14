# 完整独审：正 C 平坦出口的实际母线延拓

独立审查人：tail_review_continued_2。
原稿冻结日期2026-11-09；本次最后来源绑定检查实际发生于2026-11-10 00:02:27 UTC。
本审查没有参与被审稿推导，只读冻结来源并新建本报告。
没有执行符号程序、PDE、几何轨迹、BVP、tail、RK或网格。

**结论：接受全部显式延拓与其准确限制，没有发现阻断性数学问题或需要作者勘误之处。**
母线坐标依赖时间，但稿中确实回收了整个固定材料圆周上的共同坐标，
并支付实际周期位置、全部二阶位置数据、开重叠一致和某个全时间共同正宽的嵌入。
有限正常平坦延拓保持非零秩一第二形式；
它不能直接达到 R43 含开平面扇区的指定接口。
该限制属于这条实际正 C 平坦延拓，不是一般闭曲面或其他桥接机制的不可能性结论。

## 1. 不可变来源与已审输入

被审主稿：
[69ea0bcb043eca3d051fe020489eb418c9271466](https://github.com/Rogerhu12/math-research/blob/69ea0bcb043eca3d051fe020489eb418c9271466/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-flat-outlet-ruling-continuation-v1.md)，
路径 notes/2026-11-09-db6f-flat-outlet-ruling-continuation-v1.md，
Git blob ee9e22db31c162fb39944d2bb22696af38c3916a，
14,793 UTF-8 B，
SHA-256 b09be0f0e440ca5724c0704fd2e1975ca17f6d6056447f794f69548bd4c8fe68。
已全文读取全部8节并核完整字节与SHA。

输入的正 C 固定 H 族：
- 作者正文 ec5093a6d7c368dfaf80855d03c5c0f19ac51afe，
  blob34ba5cd303512e203a22501db57b11dd4e844470，
  SHA-256 7ea4f91fef4401f37dab9e8b4ba1228d7fe384ed70757df28bca912a157e083a。
- 完整独审
  [ab158761cb5fc844d8e2da18abdca4313aed79e6](https://github.com/Rogerhu12/math-research/blob/ab158761cb5fc844d8e2da18abdca4313aed79e6/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-positive-epicycle-bump-fixed-h-v1.md)。
- 所用单调下降 Q 定理的完整独审15b02049c367e344901fb13264a950f8ff5bf933。

R43作为已审中间结论使用。本次为核准确接口另取其正式原文：
[be7b380055c1906a1abacfc5682da0e372ef8579快照](https://github.com/Rogerhu12/math-research/blob/be7b380055c1906a1abacfc5682da0e372ef8579/topics/visible-flexible-closed-surface/results/R43-explicit-three-cylinder-flat-end-disk.md)，
路径 results/R43-explicit-three-cylinder-flat-end-disk.md，
blob e2bbfa5bffa8c56f9f25b4b8ee8f7e7d812b59c8，
18,896 B，
SHA-256 c709b5c1c130c59b769c2d6cd359f567ff545d750d17abc0f1e29c7259e8d576。
该提交只是确定含有原文的快照，不冒称R43首次采用提交。
重点重读其§§1–2、5–6和接口说明，确认共同欧氏度量与开角零II；
没有把本报告计为重新完成R43的整篇独审。

入口假设使用实际周期 gamma 和实际周期正交标架，
而不只使用周期的第二形式系数。
a_0>0、B>0在整个紧时间族中共同固定，C有统一正下界。
这里的B是平坦度量斜率，不与其他稿的弯角参数或控制变量混用。
本稿不覆盖B=0的这套极坐标公式；其他柱面入口已有各自独立表示。

## 2. V、W 标架的全部微分关系

记 p=a_0 M/C、lambda=sqrt(1+p^2)。
V=(e_1-p e_2)/lambda、W=(p e_1+e_2)/lambda 是同向正交旋转，
V×W=N，且V在入口旧径向的分量为1/lambda>0。

把原角向标架关系逐项代入，得到

\[
V'=\omega W,\qquad W'=-\omega V+kN,\qquad N'=-kW,
\]
\[
\omega=B-\frac{p'}{1+p^2},\qquad k=\frac{C\lambda}{a_0}>0.
\]

V'的法向项为(M-pC/a_0)/lambda=0；
旋转角的导数贡献正是-p'/(1+p^2)，没有漏掉lambda'。
W'的法向项为(pM+C/a_0)/lambda=C lambda/a_0。
N'也按同一p关系等于-kW。
gamma'=a_0e_2=(a_0/lambda)(W-pV)同时成立。

因此单位核方向V的法向曲率和角混合曲率确实消失。
本节不是先假设母线成立再回填第二形式。

## 3. 真实母线位置、度量和非零主曲率

定义 G(u,s)=gamma(u)+sV(u)，并令
E=-a_0p/lambda、A=a_0/lambda+s omega。
则G_s=V，G_u=EV+AW，直接给

\[
I=ds^2+2E\,ds\,du+(E^2+A^2)du^2.
\]

在入口连通的A>0分支，G_s×G_u=A N。
G_ss=0、G_su=omega W，
G_uu的法向分量为A k，因此

\[
II_{ss}=II_{su}=0,\qquad II_{uu}=Ak.
\]

由于W=(G_u-EG_s)/A，
正交切方向W的法向曲率为Ak/A^2=k/A，
而V方向为0。这验证唯一非零主曲率k/A，
不是误把坐标系数Ak本身当成主曲率。

G已经是实际空间位置公式，所有积分常数都由输入gamma给定。
但其I中的E、A随时间变化，
所以(u,s)确实不能直接当作共同材料参数。
稿中没有遗漏这个重要的材料身份问题。

## 4. 平面展开、单值角lift与完整圆周逆

令rho_0=a_0/B。
在通用覆盖中取平面单位标架
e_1^pl=e^{iBu}、e_2^pl=i e^{iBu}。
相应V^pl=e^{iBu}(1-ip)/lambda具有同样的omega旋转方程。
所以

\[
Z=e^{iBu}\{\rho_0+s(1-ip)/\lambda\}
\]

的导数具有同样E、A，第一形式恰为上节I。
它在u增加ell时乘e^{iB ell}，一般不是一个闭合平面位置图；
这与实际G的周期性并不矛盾。

对s>=0，括号实部rho_0+s/lambda严格正，
所以主值arctan给全圈一致的角修正。
写Z=(rho_0+x)e^{iB\widetilde u}后，得到稿中公式(9)，
及共同度量

\[
dx^2+(a_0+Bx)^2d\widetilde u^2.
\]

固定x解出的s_x(u)是满足s>=0的唯一根，
公式(11)和有理化后的(12)等价。
其根号始终正，不存在额外分支选择。

\[
x_s=\frac{s+\rho_0/\lambda}
 {\sqrt{\rho_0^2+2\rho_0s/\lambda+s^2}}
\]

在s>=0满足1/lambda<=x_s<=1：
分母平方与分子平方之差为rho_0^2(1-lambda^{-2})>=0，
而乘lambda^2后的反向比较由s>=0直接成立。
从s=0积分即得x<=s_x<=lambda x。

有向面积比较给

\[
(a_0+Bx)\det\frac{\partial(x,\widetilde u)}{\partial(s,u)}=A.
\]

沿固定x的圆周求导，确实得到

\[
\frac{d\widetilde u}{du}
 =\frac{A}{(a_0+Bx)x_s}.
\]

只要A>0，此导数严格正。
p、lambda、s_x的ell周期性再给
\widetilde u(u+ell)=\widetilde u(u)+ell。
所以这是度数1的严格单调圆周微分同胚，
不只是局部Jac不零。其逆覆盖整个固定材料圆周。

若lambda<=Lambda、|omega|<=Omega，
在

\[
0\le x\le h_J=\frac{a_0}
 {2\Lambda^2\max(1,\Omega)}
\]

有A>=a_0/Lambda-Lambda x Omega>=a_0/(2Lambda)>0。
并且d\widetilde u/du具有统一正下界，
例如a_0/[2Lambda(a_0+B h_J)]。
联合光滑输入、显式s_x和带参数隐函数定理因此给联合光滑逆。
共同材料表达式(16)对每个时间都严格诱导同一个g_flat。

h_J只控制坐标与浸入，不自动排除远距离空间自交。
原稿把这项与下一项全图嵌入分开是正确的。

## 5. 实际周期、C3和全部 Cartesian 两 jet

实际gamma、V周期，所以G实际周期。
逆角映射保持同一deck移位，故最终F_flat也实际周期。
这个论证不依赖平面展开Z闭合，也没有遗漏空间平移monodromy。
输入若有材料ell/3与空间120度的C3关系，
p、lambda、omega及所有角修正具有ell/3周期，
所以同一材料C3传到新图。

在x=0，s=0、u=\widetilde u。
s_u在入口为0，保持\widetilde u求x导数时
s_x=lambda、u_x=p/a_0。
代入G的两个一阶导数，得到

\[
F_x=e_1,\qquad F_{\widetilde u}=a_0e_2,\qquad F=\gamma.
\]

在入口，G的II_uu=(a_0/lambda)(C lambda/a_0)=C；
张量变换给L=M^2/C、M、C三个旧系数。
结合g_flat及其一阶导数，
Gauss公式进一步明确给

\[
F_{xx}=LN,\quad
F_{x\widetilde u}=B e_2+MN,\quad
F_{\widetilde u\widetilde u}=-a_0B e_1+CN.
\]

这些正是旧平坦领在同一径向方向的全部二阶位置导数。
所以不仅第一形式和法向二次型一致，完整Cartesian两jet也一致。
初始高度和整圈位置由gamma固定，不能另行平移调出口。

## 6. 开重叠相等，并且是同一个材料gauge

在旧C-infinity正则平坦领，C>0使II秩一且非零。
令S(V)=0、S(W)=kappa W，V单位且取入口向外方向。
Codazzi两边与V配对给

\[
-\kappa\langle\nabla_VV,W\rangle=0.
\]

V单位又给其V分量为0，所以nabla_VV=0。
II(V,V)=0，因此空间导数D_VV也为0；
同时D_VN=-S(V)=0。
故V的单位积分线确是真正空间直线，法向沿线不变。

入口横截分量1/lambda有统一正下界。
紧圆周、紧时间区间和光滑性使这些积分线在一个共同小开领形成流坐标，
其位置只能是gamma+sV。
这给旧图与G在真实开重叠上的同一位置。

还需核对从母线坐标回收后是否仍是旧材料点。
旧度量在入口领为dr^2+(a_0+Br)^2du^2，
新度量为同样形式；
两套径向坐标线都是从同一入口材料点出发、同一单位法向的内禀测地线。
在上述同一实际局部曲面上，测地线的初值唯一性迫使这两套径向法坐标相同。
等价地，可在旧平坦领的平面展开中直接使用同一个Z公式。
因此回收到(x,\widetilde u)后是同材料gauge的相等，
不是只说两张像集合相等而悄悄改变旧材料标号。

若采用旧外边界作为入口，这直接给边界两侧的C-infinity接合。
若在已有开平坦领中取固定圆周，则在重叠中识别同一材料点，
或以该固定圆周作为所保留旧域的界；没有重复附上一份重合材料。
所有旧域中的固定H点保持原材料身份和原位置。

公式在x=0附近还可向小负x光滑延拓：
根号与实部在入口均严格正，A也正，
紧输入给统一小负窗。这支付上面所用的开重叠，
不限于有限阶边界匹配。

## 7. 全时间正外宽的嵌入及新的正 reach

作者的全局嵌入论证成立。
先在共同固定小正宽中有光滑浸入，与旧图光滑相接。
若任意更小外宽都出现某时间的重复像点，
取宽度h_j下降到0和碰撞点对。
紧性给时间和参数子列极限；
至少一个点来自新段，所以其极限在入口圆周。
旧图全局嵌入迫使两个极限材料点相同。

在该入口点用一个固定线性投影把切平面投向R^2。
投影复合图的参数Jac可逆；
联合C1连续性及带参数局部逆函数定理给共同的时间/材料邻域，
其中投影映射单射。
碰撞点最终同时落入该邻域，矛盾。
这确实证明一个全时间共同h_E>0，
不是仅检查单个时间或局部Jac。

选择固定正宽不超过min(h_J,h_E)后，
整个新材料域和时间区间都紧。
全域正则性给统一的导数最小奇异值下界，
C-infinity给有限Hessian上界。
小参数差由Taylor得到弦比下界；
远离对角线的点对由全时间嵌入及紧性得到另一个正下界。
两者合并给一个全局参数弦常数gamma_*>0。

对有边带采用最短角lift上的可行直线段，
边界最近点的一侧极小条件加Taylor余项给

\[
\operatorname{reach}\ge\gamma_*^2/H_*>0.
\]

该因子已正确平方gamma_*。
常数属于整个新域和全部时间；
原稿没有给它们有效数值，也没有复用R45或原小领的3%界。
仅有A>0仍不足以宣称走到更远处不会自交，这个限制保留。

## 8. 焦集、非零II与R43的指定接口

若omega不为0，A=0的唯一母线位置为
s_foc=-a_0/(lambda omega)。
omega<0时在正s方向，omega>0时在反方向；
omega=0没有有限退化点。
k始终正，因此A趋零时几何主曲率k/A发散。
主曲率是坐标不变量，不能靠重新参数化把这个极限变成同一C2正则接口。

在入口连通的任一有限正常区域A>0，
k/A处处严格正。
若出口及时间族紧，k有正下界、A有有限上界，
从而整个出口还有统一正的非零主曲率下界。
这排除在有限正常出口出现II=0的点，更排除开角零II。

omega>0时只有s趋无穷才可能使该曲率趋零；
|G-gamma|=s且入口gamma有界，所以这不是有限空间中的紧接口。
omega=0时曲率沿母线恒定，omega<0则向外碰到上述焦集。

R43正式原文的式(5)、(9)、§5及式(18)–(21)确认：
三片活动柱弯之间存在非空开角区，
这些区域在一整个邻域是平面恒等图，所有II系数都为0。
其活动帽中心射线还可有C=0而II非零，但本次不需要以该弱事实代替开区零II。
因此当前正C母线的有限正常出口不可能与那个完整指定接口C2相接；
零/非零第二形式的区别不受刚体和材料坐标变换影响。

这只排除了当前输入经这条有限正常纯平坦延拓直接接合的办法。
它不排除加入新非平段、改变输入或使用其他桥接机制，
也不构成一般闭合不存在性。

## 9. Holonomy与端口方向的完整符号

对g_flat=dx^2+(a_0+Bx)^2du^2，
取正向正交切标架(e_r,e_u)，有
nabla_u e_r=B e_u、nabla_u e_u=-B e_r。
平行向量的分量角满足alpha'=-B，
所以绕完整材料圆周的holonomy为-B ell模2pi，
等价于通常写法2pi-B ell。

R43的共同度量正是平面欧氏度量，
其环域有全局平行Cartesian标架，holonomy为零。
在一个完整平坦连接环域内，同伦圆周的平行移动相同，
所以不能把非零的-B ell改成零。

这里“小锥角非零”是所引用正C epicycle实例的准确事实：
原已审稿给B<=2·10^-6和ell<16，
故0<B ell<32·10^-6。
本报告不把这个数值套到任意B>0的输入；
一般B ell若恰为2pi整数倍，holonomy这一项本身就不提供障碍。
前节的有限正常非零II结论则仍按其自身假设成立。

若新桥继续使用同一径向度量和u周期ell，
目标欧氏参考平面的半径R圆周在选定角向gauge中为theta=2pi u/ell
（可另有固定角相位或整体定向选择）。
因此a_out=2pi R/ell。
递增桥径向若对应目标平面极径增加或减小，
分别记epsilon_out=+1或-1，就有

\[
a'_{\rm out}=\epsilon_{\rm out}\frac{2\pi}{\ell}.
\]

内向进入圆盘不能自动使用正号。
K=-a''/a，dA=a\,dr\,du直接给

\[
\int K\,dA
 =-\ell(a'_{\rm out}-B)
 =B\ell-\epsilon_{\rm out}2\pi.
\]

epsilon_out=+1时，当前小B ell要求净负总曲率；
epsilon_out=-1时要求净正总曲率，
且a'必须从正B变到负值，确有径向转折。
这两个布局由实际接口方向决定，
不能为了符合已有存在定理而任意互换。

该预算准确限于指定共同径向gauge的桥。
它不是任意参数化、任意拓扑连接的一般曲率障碍。
匹配还要求目标实际位置、两个切向和全部II等完整Cartesian两jet，
单一半径或总曲率预算不能代替这些端点条件。

## 10. 原稿的后续研究身份与本次接受边界

原稿末尾把非减Q的再进入方法列为另行研究，符合其冻结时事实。
该新定理现在已有独立固定全文审稿
[0fbb537133c97af06cf55ca3939f002f5cfb17ad](https://github.com/Rogerhu12/math-research/blob/0fbb537133c97af06cf55ca3939f002f5cfb17ad/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-increasing-q-smooth-flat-entry-v1.md)。
它可以另行支付符合假设的正C、Q>=0非减的初始一段；
不能由此补写本稿已经完成指定边值连接。

特别是它不支付epsilon_out=-1所需的后续正曲率和径向转折，
也不自动处理最终C=0角区。
平面接口的零II和当前正C表示之间仍有真实待解部分。

本次接受实际共同材料平坦延拓、全圈位置与材料C3、
完整二jet及开重叠全jet、保留旧H、
某个全时间共同正宽嵌入和新的定性正reach、
焦集及有限平坦接合限制、holonomy和带方向的曲率预算。
没有计算有效h_E、归一reach、像幅度或最终接缝。
没有凭保留旧域自动扩张任何未在本文证明的新整图指标。

## 11. 实际证据与未运行项目

主稿完整文本绑定在JavaScript/V8隔离运行时独立核对：
运行身份tail-review-flat-outlet-source-binding-01，
clock实际时间2026-11-10 00:02:27 UTC，
完整14,793 B与SHA b09be0f0…一致。
R43完整18,896 B、blob和SHA也已单独核到固定正式原文。

本次数学审核是上述逐项微分、全圈拓扑、几何唯一性、
全局嵌入、边界最近点和接口论证。
**没有新符号程序或其他数学程序实际运行**；
没有把旧输入的任何程序回执转移给本文。
只有小文本获取、完整哈希及保存/固定读回操作。

所有文件只以新小文本保存，作者原文和正式results均保持不动。
本报告不声明闭曲面、0.05D幅度、指定R43桥、
主轨迹G5或最终独立整链完成。
