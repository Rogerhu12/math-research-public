# 有符号曲率闭嵌入种子：全文、整数外向算法及实际独立重跑审稿

审者：Astra-visible-flex-78718bd0 / independent_audit，2026-11-10。
审者未参与该曲线的参数选择、浮点初探、对称构造、证明或源程序编写；
本审也不涉及主 M14 数值候选的种子选择、调参或优化。

## 0. 冻结对象、实际重跑与审查结论

逐节全文审查：

- [geometry-signed-torsion-seed-v1](2026-11-10-78718-geometry-signed-torsion-seed-v1.md)，
  10297 B，SHA256
  64ec52db4d0b1fe6fdc704f459370da9b63280f9fddc23a8ac13c91ceb8f59e5。
- [冻结整数区间源](../scripts/78718-geometry-signed-torsion-seed.py)，
  6208 B，SHA256
  2eb4e37f881214e2857a22b236a3d4af08f9bf61ea7e3c7a25470e008114b800。

**全文第 1—7 节及完整源程序独审通过，没有阻断缺口。**
该结论同时依靠下文的全部解析论证、逐个外向运算与余项核查，以及
实际执行冻结源，绝不是只读源码或只看作者报告。

审者在执行前实际核对源文件长度和 SHA256，随后用独立报告路径运行
冻结源。终端回执 c57034，自然退出码 0，状态为
PASS_EXACT_OUTWARD_DYADIC_CURVE_SEED_ONLY。审者报告为
[独立区间重跑回执](2026-11-10-78718-audit-signed-torsion-seed-replay.json)，
1287 B，SHA256
3426677948edd0a1da6f2998d3be64256e0a6c2f82bd5bb379cd3eaefb6d5b58。

作者原报告为
[原始区间回执](2026-11-10-78718-geometry-signed-torsion-seed-check.json)，
1287 B，SHA256
61eb32fa11aa4ec437c11d2c9318522dac585a154895f89c8d8762aeabfe5942。
本次另在终端内逐字段比较两份报告：除起止时间外所有字段精确一致，
包括源身份、区间端点和严格门；独立再以 Fraction 读取端点，确认
最大 f 上端小于 0、X 下端大于 1/2、Y 上端小于 -1。
端点数据没有输出到对话。

正式转录只需两处文字整理：

1. 式 (9) 第二行的 “quad” 补为 “\quad”。
2. §3.2 的“24 阶偶多项式”最好明确为：关于 \(x^2\) 的 24 次
   多项式，亦即关于 \(x\) 的 48 次偶多项式，共 25 个系数。
   原稿明确的有限和、阶数 50 的余项及实际代码一致，没有数学错误。

本结论是一个实际解析闭嵌入曲线及全周期标架、一个实际直纹参考度量，
以及可通过首个必要周期 jet 方程的边界数据族。**没有任何二维非平凡
等距延伸、帽、闭曲面或有效幅度在此得到证明。**
本审实际运行的是曲线函数的区间代数与积分包围；
曲面 ODE/PDE、优化、网格或主数值候选执行数均为 0。

## 1. 解析球面曲线与非零速度

记原稿常数 \(a=2\sqrt6/5>0\)，令
\[
 z=a\cos t,\qquad \rho=\sqrt{1-z^2},\qquad
 \vartheta=2t+\frac{13}{6}\sin2t,
\]
\[
 B=(\rho\cos\vartheta,\rho\sin\vartheta,z).
\]
因为 \(a^2=24/25\)，
\(\rho^2=1-(24/25)\cos^2t\ge1/25\)。
正平方根在这个严格正区间上解析，故 \(B\) 在整圈解析且 \(|B|=1\)。

以水平极坐标单位向量 \(e_r,e_\theta\) 表示，
\[
 B=\rho e_r+ze_z,\qquad
 B_t=\rho'e_r+\rho\vartheta'e_\theta+z'e_z,\qquad
 \rho'=-zz'/\rho.
\]
所以
\[
 |B_t|^2=\rho'^2+\rho^2\vartheta'^2+z'^2
 =\frac{z'^2}{\rho^2}+\rho^2\vartheta'^2.
\]
只有 \(t\in\pi\mathbb Z\) 时 \(z'=0\)；在这些点
\(\vartheta'=2+13/3=19/3\)，\(\rho=1/5\)，故右端仍严格正。
因此 \(v=|B_t|\) 为严格正的解析周期函数。

定义
\[
 \gamma(t)=\int_0^tB(q)\times B_q(q)\,dq.
\]
因 \(B\cdot B_t=0\)、\(|B|=1\)，
\(|\gamma_t|=|B\times B_t|=|B_t|=v>0\)。
所以它是实际解析正则空间曲线；后面仍需证明闭合和全局单射，不能只从
球面曲线闭合就宣称这些性质。

## 2. 三个位置分量的完整闭合

令 \(J_z=\operatorname{diag}(1,1,-1)\)，
\(S_z=-J_z=\operatorname{diag}(-1,-1,1)\)。
因 \(\rho(t+\pi)=\rho(t)\)、\(\vartheta(t+\pi)=\vartheta(t)+2\pi\)、
\(z(t+\pi)=-z(t)\)，
\[
 B(t+\pi)=J_zB(t),\quad B_t(t+\pi)=J_zB_t(t).
\]
反射矩阵的叉乘规则给
\[
 \gamma_t(t+\pi)
 =\det(J_z)J_z(B\times B_t)=S_z\gamma_t(t).
\]
两个水平速度分量在半周期后反号，因此整周期的水平位移精确为零。

竖分量为 \(\gamma_{z,t}=\rho^2\vartheta'\)。
设 \(c=\cos2t\)，则
\(\rho^2=(13-12c)/25\)，
\(\vartheta'=2+(13/3)c\)。直接相乘并以
\(c^2=(1+\cos4t)/2\) 化简：
\[
 \rho^2\vartheta'
 =\frac{26}{25}+\frac{97}{75}c-\frac{52}{25}c^2
 =\frac{97}{75}\cos2t-\frac{26}{25}\cos4t.
\]
常数项精确消失，故竖向整周期位移也为零。积分得
\[
 \gamma_z(t)=\frac{97}{150}\sin2t-\frac{13}{50}\sin4t
 =\sin2t\left(\frac{97}{150}-\frac{13}{25}\cos2t\right).
\]
括号的全局下界为 \(19/150>0\)。因此四个开四分区内的竖坐标符号依次
为正、负、正、负；其零点正好是四分点。

这证明 \(\gamma(2\pi)=\gamma(0)\)，并且 \(\gamma_t\) 本来解析周期，
所以全部导数 jets 匹配，\(\gamma\) 是材料圈上的解析曲线。

一般参数来源也正确：若
\(\vartheta=2t+c_0\sin2t\)、\(z=a\cos t\)，则
\(\rho^2\vartheta'\) 的平均为 \(2-a^2-c_0a^2/2\)。
其为零给 \(c_0=4/a^2-2\)；代入 \(a^2=24/25\) 正好得到 \(13/6\)。
本审没有重新选择或调整这些参数。

## 3. 水平速度及在端点正则的符号函数

利用第 1 节的水平极坐标表达，
\[
 B\times B_t
 =(z\rho'-\rho z')e_\theta-z\rho\vartheta'e_r
   +\rho^2\vartheta'e_z.
\]
由 \(z\rho'-\rho z'=-z'/\rho=a\sin t/\rho\)，得
\[
 \gamma_{x,t}
 =-a\left(\frac{\sin t}{\rho}\sin\vartheta
          +\cos t\,\rho\,\vartheta'\cos\vartheta\right),
\]
\[
 \gamma_{y,t}
 =a\left(\frac{\sin t}{\rho}\cos\vartheta
         -\cos t\,\rho\,\vartheta'\sin\vartheta\right).
\]
故源码 values 中 vx、vy 的符号、系数和导数变量都与真实曲线一致。

对于 \(0<t\le\pi/2\)，
\[
 \frac{\sin\vartheta}{\sin t}
 =\frac{\vartheta}{t}\,
   \frac{\operatorname{sinc}\vartheta}{\operatorname{sinc}t},
\quad
 \frac{\vartheta}{t}=2+\frac{13}{3}\operatorname{sinc}(2t).
\]
因此源码中的
\[
 f=\cos\vartheta-\cos t\,\rho^2\vartheta'
      \left(2+\frac{13}{3}\operatorname{sinc}(2t)\right)
      \frac{\operatorname{sinc}\vartheta}{\operatorname{sinc}t}
\]
确实等于 \(\rho\gamma_{y,t}/(a\sin t)\)。
这个公式没有除以 \(t\) 或 \(\sin t\)，在 \(t=0\) 采用 sinc 的解析
延拓，其值正好是
\[
 f(0)=1-\frac1{25}\left(\frac{19}{3}\right)^2
 =-\frac{136}{225}.
\]
另一端 \(t=\pi/2\) 同样正则。符号证书覆盖闭区间的 \(f\)，但由它推出
\(\gamma_{y,t}<0\) 的范围准确是 \(0<t\le\pi/2\)；
在 \(t=0\) 该速度本身为 0，不曾误称严格负。

下面核查程序确实在整个连续区间证明 \(f<0\)，而非只在一组采样点证明。

## 4. 全部外向基本运算

令 \(S=2^{128}\)。I(lo,hi) 表示闭区间
\([\mathrm{lo}/S,\mathrm{hi}/S]\)，构造器检查 \(\mathrm{lo}\le\mathrm{hi}\)。
所有数学数据只用 Python 任意精度整数和 Fraction；时间戳仅用于报告，
没有进入数学运算。

I.q 首先精确形成 Fraction，分母规范为正；下端是有理数乘 \(S\) 的
向下整除，上端用 ceildiv(a,b)=-((-a)//b) 向上整除。
该恒等式对正负分子都成立，所以也正确包围 Taylor 的负系数。

加法以两个下端、两个上端相加；取负交换端点并取负；减法由加负数实现。
整数无溢出，故这些步骤精确。

乘法列出四个端点积，其最小值、最大值给真实双线性乘积的范围。
实际表示端点需要从 \(S^2\) 缩回 \(S\)，因此分别向下、向上除以 \(S\)。
即使两个因子来自同一变量、一个区间跨过零，独立区间乘法仍包含
所有真实相关值；它可能扩大范围，不能漏掉真实值。

除法先断言分母下端严格正。倒数的缩放端点
\[
 \left\lfloor\frac{S^2}{\mathrm{hi}}\right\rfloor,\qquad
 \left\lceil\frac{S^2}{\mathrm{lo}}\right\rceil
\]
正是倒数区间的外向端点，再使用已核对的乘法。
代码未对跨零分母使用不合法倒数。

平方根要求 lo 非负。缩放后的精确端点应为
\(\sqrt{\mathrm{lo}\,S}\)、\(\sqrt{\mathrm{hi}\,S}\)。
isqrt 给下取整整数；上端在非完全平方时加一。
因此无论端点是否为平方数，都具有正确包含性。

实际 values 中的除数只有 rho 和 sinc(t)，均经运算的正下端检查；
rho2 还在开方前另断言严格正。每个盒中的这些断言都在实际重跑中通过，
不能把分母的“真值应为正”误代替机器区间的合法性检查。

## 5. π、Horner 与每个解析余项

### 5.1 Machin 区间

arctan_bounds 对 \(q=5,239\) 使用
\[
 \arctan(1/q)=\sum_{k\ge0}\frac{(-1)^k}{(2k+1)q^{2k+1}}.
\]
项的绝对值严格递减至 0。精确 Fraction 部分和与加上第一遗漏项的值
因此包围真实函数；取 min/max 同时适用于奇数或偶数项数。
源码实际分别采用 40、12 项。

Machin 恒等式的分支也可独立支付。令
\(A=\arctan(1/5)\)、\(B_0=\arctan(1/239)\)。
两次倍角给
\[
 \tan(2A)=5/12,\qquad \tan(4A)=120/119.
\]
再由减角公式，\(\tan(4A-B_0)=1\)。
有 \(A>B_0>0\)，且
\(1/5<\tan(\pi/8)=\sqrt2-1\)，故
\(0<4A-B_0<4A<\pi/2\)。所以该角确实为 \(\pi/4\)，不是仅模
\(\pi\) 的等式。于是 \(\pi=16A-4B_0\)。

因此代码 low=16*a0-4*b1、high=16*a1-4*b0 的上下搭配正确。
两个精确有理界最终各自外向转为 dyadic 端点；实际额外断言
\(3<\mathrm{low}<\mathrm{high}<22/7\) 也通过。

### 5.2 余项与多项式包含性

源码每次调用 even_taylor 都断言输入区间的全部端点绝对值不超过 6。
区间已经包含真实函数参数，故这个检查真实支付余项所用的整个参数域。
它适用于 t、2t、theta 的所有实际调用；没有未经校验的区间外插。

TERMS=24，系数 k 从 0 到 24，共 25 项。
cos 的多项式次数为 48；对 cos 使用至 49 次 Taylor 展开时，
49 次系数为 0，因此
\[
 \left|\cos x-\sum_{k=0}^{24}
   \frac{(-1)^kx^{2k}}{(2k)!}\right|
 \le\frac{|x|^{50}}{50!}\le\frac{6^{50}}{50!}.
\]
这是 Taylor 定理的全实域余项界，不要求交错项在当前 x 上单调。
不能错误地只用“下一交错项”而不说明这一点；实际源码并没有此问题。

又
\(\operatorname{sinc}x=\int_0^1\cos(sx)\,ds\)。
对上述余项积分，得到
\[
 \left|\operatorname{sinc}x-\sum_{k=0}^{24}
  \frac{(-1)^kx^{2k}}{(2k+1)!}\right|
 \le\frac{|x|^{50}}{51!}\le\frac{6^{50}}{51!}.
\]
所以代码中的 degree=2*TERMS+2=50，以及 cos 用 50!、sinc 用 51!，
全部正确。

xx=x*x 是对实际 \(x^2\) 的包含区间；每个有理系数由 I.q 外向包围。
Horner 的每次乘加都采用第 4 节已经证明的包含运算，归纳即得最终
result 包围整个多项式值域。
余项半径用精确 Fraction 形成，然后将它乘 \(S\) 向上整除；
从下端减去该整数、向上端加上它，故两侧都包含真实余项。
sin 则以 x*sinc(x) 的区间乘法给出，没有额外遗漏的求值误差。

## 6. 连续覆盖、Darboux 积分与实际执行

令 \(h_\pi=\pi/2\)，真实参数写为 \(t=h_\pi x\)、\(0\le x\le1\)。
BOXES=1024。因为 \(1024\mid2^{128}\)，实际 x_box 的端点
\(j/1024,(j+1)/1024\) 甚至是精确 dyadic；源码的向下、向上整除也
普遍保持包含性。

对每个闭盒，t=half_pi*x_box 包含所有对应真实 t。
包含 π 的不确定性只扩大该区间，并不会在相邻真实材料盒之间留下空隙。
第 4—5 节的归纳包含性说明 values(t) 的三个输出分别包围真实 f、
水平 x 速度、水平 y 速度在整盒的全部取值。
实际每盒 f.hi<0 的断言全部通过，因此闭区间上处处 f<0。

对任一速度分量 V，
\[
 \int_0^{\pi/2}V(t)\,dt
 =\sum_{j=0}^{1023}\int_{j/1024}^{(j+1)/1024}
    h_\pi V(h_\pi x)\,dx .
\]
各盒已包围 V 的全部取值；把该区间与包含真实正 \(h_\pi\) 的 half_pi
相乘，再乘精确正宽度 \(1/1024\)，便包含该盒真实积分。
即使 V 区间有负数，完整的四端点乘法也正确。
逐盒外向相加就是有效上下 Darboux 包围，无需未说明的数值求积误差。
重复使用同一个 π 或同一个常数 a 的相关性只可能让区间更宽，不损坏包含性。

源码用纯整数比较检查
integral_x.lo>SCALE//2 与 integral_y.hi<-SCALE；
SCALE 为偶数，SCALE//2 精确表示 1/2。
结合逐盒 f 门，实际证明
\[
 f<0\text{ 于 }[0,\pi/2],\qquad X>1/2,\qquad Y<-1.
\]
独立执行通过，报告绑定冻结源哈希；独立读取回执的精确有理门也通过。
原作者选择参数时的浮点初探没有被使用为这些门的证明。

本次实际命令的等价 argv 是：

python topics/visible-flexible-closed-surface/scripts/78718-geometry-signed-torsion-seed.py
--report topics/visible-flexible-closed-surface/notes/2026-11-10-78718-audit-signed-torsion-seed-replay.json

实际执行由终端 Python subprocess 在预先断言冻结源身份后调用；
不是复制原报告，也不是把源码静态审查当作运行。

## 7. 四分弧、所有端点与整个集合嵌入

令 \(J_y=\operatorname{diag}(1,-1,1)\)。
由 rho、z 偶而 theta 奇，
\(B(-t)=J_yB(t)\)，微分时必须带链式负号：
\(B_t(-t)=-J_yB_t(t)\)。
因此
\[
 \gamma_t(-t)=J_y\gamma_t(t),\qquad
 \gamma(-t)=-J_y\gamma(t)=S_y\gamma(t),
\]
其中 \(S_y=\operatorname{diag}(-1,1,-1)\)。
这个速度与位置的符号差别已独立核对。

积分第 2 节半周期速度关系，得到
\[
 \gamma(t+\pi)=\gamma(\pi)+S_z\gamma(t).
\]
再结合上式的反射，
\[
 \gamma(\pi-t)=\gamma(\pi)+S_zS_y\gamma(t)
 =\gamma(\pi)+S_x\gamma(t),
\quad S_x=\operatorname{diag}(1,-1,-1).
\]
在 \(t=\pi/2\) 代入，因该点 z=0，
\[
 \gamma(\pi)=(0,2Y,0).
\]
四个四分端点依次为
\[
 (0,0,0),\quad(X,Y,0),\quad(0,2Y,0),\quad(-X,Y,0).
\]
\(Y<-1\) 区分 y 层，\(X>1/2\) 区分同一 y 层的两个中端点；
因此四者全部不同。这个 X 门不能由 z 的符号或 y 单调性代替。

第一开四分弧的 y 严格递减，所以单射；
它的 y 在 \((Y,0)\)，z 严格正。
其它三弧是该弧的参数反向或正向刚体像，分别满足：

| 开材料弧 | y 范围 | z 符号 |
| --- | --- | --- |
| 第一四分弧 | (Y,0) | 正 |
| 第二四分弧 | (2Y,Y) | 负 |
| 第三四分弧 | (2Y,Y) | 正 |
| 第四四分弧 | (Y,0) | 负 |

这四个开区域两两不交，所以不同开弧不相交。
各弧内部的 z 不为零，所以也不可能撞上任何 z=0 的四分端点。
端点已逐一排除重合，只剩材料圈本来就识别的 0 与 \(2\pi\)。
由此得到圈上的全局单射；结合正则性与紧性，确为解析闭嵌入。

## 8. 曲率零点处仍合法的周期标架

以共同正速度定义
\[
 u(t)=\int_0^t v(q)\,dq,\qquad \ell=u(2\pi).
\]
v 严格正且解析，故 u 给解析材料圈坐标，并且
\(|B_u|=1\)。由积分定义，
\[
 T=\gamma_u=B\times B_u,\quad
 d=-B_u,\quad N=d\times T=-B.
\]
B 与 \(B_u\) 单位且正交，所以 \((d,T,N)\) 是全圈解析、正定向、
正交标架。其定义从未除以 \(|T_u|\)，因此普通曲率为零时依旧合法；
全部向量随 t 周期，故作为 u 的函数也有精确周期和全部 jets 匹配。

从 \(d\cdot B=0\) 微分：
\(d_u\cdot B=-d\cdot B_u=1\)，所以
\[
 \beta=d_u\cdot N=-1.
\]
又 \(T_u=B\times B_{uu}\)，故 \(T_u\cdot N=0\)，即边界
\(\kappa_D=0\)。剩余标架系数为
\[
 \alpha=d_u\cdot T
 =-\det(B,B_u,B_{uu})
 =-\frac{\det(B,B_t,B_{tt})}{v^3}.
\]
最后等式中的 \(v_t B_t\) 项因两列相同而消失。
于是实际系统确实是
\[
 d_u=\alpha T-N,\qquad T_u=-\alpha d,\qquad N_u=d.
\]

在普通曲率非零的一个连通区间，令
\(\sigma=\operatorname{sgn}\alpha\)，则
\[
 k_F=|\alpha|,\qquad n_F=-\sigma d,\qquad b_F=\sigma N.
\]
故 \((b_F)_u=\sigma d=-n_F\)，真实 Frenet 扭率为 1。
这严格证明了原稿在非零曲率区的说法；在零点处不套用未定义的 Frenet
商式，不声称普通 Frenet 标架在该点仍唯一。
所谓全圈常扭率的无歧义内容是已明写的光滑标架系统 \(\beta=-1\)。

对直纹参考图 \(F(r,u)=\gamma(u)+rd(u)\)，在 \(r=0\)
有 \(F_r=d,F_u=T\) 和法向 N，因此
\[
 L=F_{rr}\cdot N=0,\quad
 M=d_u\cdot N=-1,\quad
 C=T_u\cdot N=0,\quad K=-1.
\]
它给真实渐近边界数据及其参考度量，并未宣称已构造一族非平凡二维解。

## 9. 零积分、真实变号和首个必要周期门

由 \(B(t+\pi)=J_zB(t)\)，v 有半周期 \(\pi\)；
因此 \(u(t+\pi)=u(t)+\ell/2\)。
三重积的三列都乘同一反射 \(J_z\)，其符号反转，而 \(v^3\) 不变，
所以
\[
 \alpha(u+\ell/2)=-\alpha(u),\qquad
 \int_0^\ell\alpha(u)\,du=0.
\]
这支付真实弧长测度下的积分，不能仅以 t 的无权平均替代。

还需排除 \(\alpha\equiv0\)。在 t=0，
\[
 B=(1/5,0,a),\quad
 B_t=(0,19/15,0),\quad B_{tt}=(-29/9,0,-a).
\]
这里 rho''=24/5 与 theta'=19/3 给
\(B_{tt,x}=24/5-(1/5)(19/3)^2=-29/9\)，故导数数值正确。
三重积为 \(2584a/675\)，\(v^3=6859/3375\)，得到
\[
 \alpha(0)=-\frac{680a}{361}\ne0.
\]
半周期反号使它确实变号。非恒零解析函数在紧解析圈上的零点孤立，
由紧性只能有限个；本稿不需要这些零点为简单零点。

参考度量确实为
\[
 a_g^2=(1+r\alpha)^2+r^2
\]
，因为 \(\beta=-1\)。此前已独审的边界首 jet 方程在这里成为
\[
 -2L_0'=\alpha L_0^2.
\]
令 \(A(u)=\int_0^u\alpha(s)\,ds\)。
A 解析、周期且有界；所以
\[
 L_{0,\lambda}(u)
 =\frac{\lambda}{1+(\lambda/2)A(u)}
\]
对全部充分小实 \(\lambda\) 分母全圈不为零，直接微分验证该方程。
零参数给零解，非零充分小参数给实际有限解析周期边界函数。
函数值和全部 u 导数的周期性来自 A 的真实周期，非仅端点凑值。

因此本稿确实提供了一个闭嵌入空间曲线及周期标架，通过首个有符号积分门。
它没有支付 L、M、C 的二维延伸或更高法向兼容条件；不能把这一解族
升级为有相同度量的实际曲面族。

## 10. 文献关联、实际范围与采用建议

原稿作为背景引用的 Bates–Melko 文章已通过 arXiv 的 HTML 正文核查：
[On curves of constant torsion I，§1 及 §1.1](https://arxiv.org/html/1206.7086v1)。
其中确有球面副法向积分表示，并讨论带标架的有符号曲率。
本审只把它作为表示式的背景出处；新曲线的闭合、嵌入、符号与周期积分
全部由本审第 1—9 节和独立区间执行重新证明，不借文中图像或其它种子的
性质。没有下载、上传或逐页渲染 PDF。

可正式采用：

- 指定公式给实际解析闭嵌入空间曲线；
- 指定解析周期标架在全部普通曲率零点仍存在；
- 常标架系数 beta=-1，渐近边界 C=0，非零区真实 Frenet 扭率为 1；
- alpha 真实变号、零点有限，且弧长周期积分严格等于零；
- 明示的一参数边界函数通过首个必要周期 Riccati 门；
- 全连续四分弧符号与积分门由完整外向算法及真实独立运行支付。

正式转录修复式 (9) 的排版，并明确多项式次数即可。
没有任何理由在此增加主问题的正则性门，也没有完成二维帽、闭曲面、
有效大幅度或 M14 数值最终证书。
