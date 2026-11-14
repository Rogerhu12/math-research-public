# R187：单位闭合角切向量给出的直接位置入口

**状态：完整函数、闭合、角向等距、边界两jet和实际metric导数公式已证明。纯JavaScript首次实际初值计算已完成；所有非圆初值仍有显著metric误差，没有非线性解或强闭曲面证书。**

本结果另开以真实空间位置为未知量的入口。它保留主线的实际几何要求，不把形式GC场、小残差或单元作为闭曲面。它不修改34接受态、36mid有限目标或独立B32的GC求解。

## 1. 完整单位切向量及准确闭合

令 $s\in[c,S]$，$u\in\mathbb R/(2\pi\mathbb Z)$。给定正函数 $a(s)$ 及两个真实角函数
$$
\Theta(s,u)=u+\vartheta(s,u),\qquad \Phi(s,u),
$$
其中 $\vartheta,\Phi$ 关于 $u$ 都是奇函数且具有周期 $\pi$。例如可以由满足同样对称性的已知完整lifting加有限和
$$
\sum_{j,k}A_{jk}B_j(s)\sin(2ku),\qquad
\sum_{j,k}B_{jk}^{*}B_j(s)\sin(2ku)
$$
给出；实际三角复合始终作为完整函数，不截掉其产生的高角频。

定义
$$
T=(-\sin\Theta\cos\Phi,\ \cos\Theta\cos\Phi,\ \sin\Phi).
\tag{1}
$$
直接有 $|T|=1$。前两分量在 $u\mapsto u+\pi$ 下反号，第三分量关于 $u$ 为奇函数。因此
$$
\int_0^{2\pi}T(s,v)\,dv=0.
\tag{2}
$$
这不是采样平均为零或有限DFT的近似条件。

对任意零均值周期向量函数 $V$，定义唯一零均值周期primitive
$$
\mathcal P V(u)=\int_0^uV(v)\,dv
-\frac1{2\pi}\int_0^{2\pi}(2\pi-v)V(v)\,dv.
\tag{3}
$$
其导数为 $V$，且平均为零。取 $Y=\mathcal P T$ 与任意轴向中心 $Z(s)$，令
$$
X(s,u)=a(s)Y(s,u)+Z(s)e_z.
\tag{4}
$$
由(2)–(3)，每个实际材料圈准确闭合。由 $X_u=aT$，
$$
|X_u|^2=a^2
\tag{5}
$$
在所有物理点准确成立，无需Gauss方程、角向投影或另外求闭合周期。

(1)是一个明确的对称候选类；不声称涵盖所有嵌入或所有轴对称度量的解。任意角参数值都给闭合的单位切向量，但仍须检查由(4)得到的曲面是否浸入、嵌入，以及剩余metric条件。

## 2. 剩下的真实度量方程及完整Jacobian

设
$$
V=X_s=a_sY+aY_s+Z_se_z.
$$
相对同一目标 $g=ds^2+a(s)^2du^2$，实际归一误差矩阵为
$$
B=
\begin{pmatrix}
r_E&r_F\\r_F&0
\end{pmatrix},
\qquad
r_E=|V|^2-1,\quad r_F=V\cdot T.
\tag{6}
$$
因为原交叉项为 $X_s\cdot X_u=aV\cdot T$，(6)完整保留它。故只需求真实位置的两项
$$
r_E=0,\qquad r_F=0.
\tag{7}
$$
其最大相对二次型误差准确为
$$
\|B\|_{\rm op}
=\frac{|r_E|}{2}+\sqrt{\frac{r_E^2}{4}+r_F^2}.
\tag{8}
$$
不能以一个投影范数替代(8)的全域上确界。实际Gram行列式为
$a^2(1+r_E-r_F^2)$；它正才有局部浸入。

完整三角导数为
$$
T_\Theta=(-\cos\Theta\cos\Phi,-\sin\Theta\cos\Phi,0),
$$
$$
T_\Phi=(\sin\Theta\sin\Phi,-\cos\Theta\sin\Phi,\cos\Phi).
$$
对于任意状态或物理参数变化，
$$
\delta T=T_\Theta\delta\Theta+T_\Phi\delta\Phi,\quad
\delta Y=\mathcal P\delta T,
$$
$$
\delta V=\delta a_sY+a_s\delta Y+\delta aY_s
+a\mathcal P\delta T_s+\delta Z_se_z.
\tag{9}
$$
这里固定物理 $s,u$；所有lifting依赖必须进入相应变化，不能只微分raw系数。

写
$$
T_s=T_\Theta\Theta_s+T_\Phi\Phi_s,
$$
则
$$
\begin{aligned}
\delta T_s={}&T_\Theta\delta\Theta_s+T_\Phi\delta\Phi_s\\
&+(T_{\Theta\Theta}\Theta_s+T_{\Theta\Phi}\Phi_s)\delta\Theta\\
&+(T_{\Theta\Phi}\Theta_s+T_{\Phi\Phi}\Phi_s)\delta\Phi .
\end{aligned}
\tag{10}
$$
二阶导数直接为
$$
T_{\Theta\Theta}=(\sin\Theta\cos\Phi,-\cos\Theta\cos\Phi,0),
$$
$$
T_{\Theta\Phi}=(\cos\Theta\sin\Phi,\sin\Theta\sin\Phi,0),
\qquad T_{\Phi\Phi}=-T.
$$
最终真实残差列为
$$
\delta r_E=2V\cdot\delta V,\qquad
\delta r_F=\delta V\cdot T+V\cdot\delta T.
\tag{11}
$$
完整primitive与参数微分交换来自紧域上的连续导数及(2)的参数恒等式。有限积分误差仍要另计；不能将数值primitive的离散导数冒准确 $T$。

## 3. C²两端lifting与真实曲率

若 $a,Z,T$ 有所需连续二阶导数，则(3)–(4)给完整C²位置图。其真实二阶导数为
$$
X_{uu}=aT_u,\qquad X_{su}=a_sT+aT_s,
$$
$$
X_{ss}=a_{ss}Y+2a_sY_s+a\mathcal P T_{ss}+Z_{ss}e_z.
\tag{12}
$$
由(12)和真实第一基本形式计算法向与主曲率，不用形式II替换。

给定两端真实 $T,T_s,T_{ss}$ 以及 $a,a_s,a_{ss}$ 和 $Z,Z_s,Z_{ss}$，(3)、(4)、(12)即确定对应的完整位置0–2jet。若两端来自同一对称实际中央柱/尾，并选定一致的中心，匹配这些完整函数就匹配真实位置两jet；不是只匹配若干角点。

在水平切向投影不为零的端口，可用连续角支把实际端口及其两个径向导数转为 $\Theta,\Phi$ 的两jet。端角函数减 $u$ 后和 $\Phi$ 保持上述奇性/周期。六个标准quintic Hermite权重逐点lift它们，再加入端点0–2jet全零的C²径向基，仍保完整端口和闭合。

例如归一坐标 $x=(s-c)/(S-c)$、$L=S-c$，左端三权重为
$$
1-10x^3+15x^4-6x^5,
$$
$$
L(x-6x^3+8x^4-3x^5),\qquad
\frac{L^2}{2}(x^2-3x^3+3x^4-x^5),
$$
右端三权重为
$$
10x^3-15x^4+6x^5,
$$
$$
L(-4x^3+7x^4-3x^5),\qquad
\frac{L^2}{2}(x^3-2x^4+x^5).
$$
各对应端点的0/1/2阶物理导数是单位矩阵，另一端全零。角对称性由线性组合保留。
可用紧支撑C²三次B-spline作后续修正；不能用仅C0的径向P1角场冒C²位置图。

实际平尾圆盘 $X=(r\cos u,\gamma_y(r\sin u),\gamma_z(r\sin u))$ 也可作为端口。
必须消费其真实0–2jet及径向平均中心，不能把非平尾的 $Z_s,Z_{ss}$ 强置为零。
下面唯一已执行实验只使用零尾的平圆盘端口，不预付非零尾实现。

## 4. 一个闭合、保角向长度的显式初值

令 $\Gamma(u)$ 为中心在原点、同样反射对称的平面闭曲线，满足 $|\Gamma_u|=a_0$。
写 $e=(\cos u,\sin u)$，$v_0=e_u$、$v_1=\Gamma_u/a_0$。
取连续相对切角 $\delta(u)$，使 $v_1$ 由 $v_0$ 平面旋转 $\delta$ 得到，
并令
$$
h(u)=2\sin(\delta(u)/2),\qquad H'=h,\qquad \int_0^{2\pi}H=0.
$$
对本文等弧长椭圆，$\delta$ 奇且π周期，所以 $h$ 零均值，$H$ 存在且光滑。
又有
$$
|v_1-v_0|^2=h^2.
\tag{13}
$$

取径向角 $\beta(s)$：中央柱上为π，cut邻端为0，并在两个接头保径向1/2阶导为0。
设
$$
q=\frac{1-\cos\beta}{2},\qquad r=\frac{\sin\beta}{2}.
$$
定义完整位置
$$
X_{xy}=a\left((1-q)e+q\Gamma/a_0\right),\qquad
X_z=Z_b+arH.
\tag{14}
$$
其角切向量除以 $a$ 为
$$
T=((1-q)v_0+qv_1,\ rh).
$$
由(13)和 $r^2=q(1-q)$，
$$
|T|^2=1-q(1-q)|v_1-v_0|^2+r^2h^2=1.
\tag{15}
$$
因此(14)是(5)的另一个显式完整函数实现。它不是将一般曲面的角向误差投影掉，而是从定义上构造准确单位角切向量。

中央保护区 $a=a_0,\beta=\pi$ 给真实椭圆柱；零尾cut处 $\beta=0$ 给原圆参考及其两jet。
本实验取
$$
\beta=\pi(1-S_5((s-c)/(S-c))),\qquad S_5(t)=10t^3-15t^4+6t^5
$$
于过渡区，外侧常值。端点二阶平坦使上述拼接C²。
完整 $E,F$ 一般不为目标值；(15)不消除它们，初值仍必须真正求解。

该显式初值可在水平切向投影不为零时转换为(1)的两角，再用第2节完整Jacobian优化。
允许完整两角修正比只调一个径向 $\beta(s)$ 更宽；后者不是一般解的充分参数化。

## 5. 相位族、固定区域与最终几何的限定

若最终 $X$ 满足完整共同g，并有需要的固定圆周等变邻域，可定义
$$
F_\alpha(s,u)=R_z(-\alpha)X(s,u+\alpha).
$$
由于目标g与u无关，真实相对metric误差在每一相位仅作角平移；
整个全角上确界相同。C²图在紧材料域上的平移及刚体旋转给C²时间连续。
在 $X=a(s)e(u)+Z(s)e_z$ 的整个邻域，$F_\alpha=X$，可接逐点固定的帽。

这些是条件结论。当前有限角网格的最大值不是全角上确界，也没有自动证明任意相位的嵌入、非局部reach、H大小、held或含反射商距离。真实闭帽/非零尾/全部强比例仍按R126/R168/R179及本题README支付。

## 6. 唯一实际初值实验和精确范围

输入是已main的R181 B32候选：
`notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json`，
SHA256 `9c903de99a0ca295db7d99e4dfec837db7778a7e20bc07abd6035a63e59a938d`。

源码 `scripts/fd2d-direct-position-tangent-lift-baseline-R187.cjs`，
12898B，SHA256 `ca06fd0651f9479a0f66ea3090d450d695e3f2383d64874bd6ce11eb8698d3bf`，
首次保存main d5fc5baa6ebea8709f18cac79914b2e8dcd87774。
它实际执行于functions的V8，560毫秒；没有OS子进程，不登记虚构exit0。
随后保存源码与实际执行字符串逐字相同；不是恢复后重跑。

该有限求值恢复60个原片，得
$a_0\approx1.004082838021469$、$S_{\rm float}\approx.8856739498716915$、
圆背景高约 $.743536989256208$、deep-coast约 $.0011804378435995079$。
使用24点phase求积、椭圆quarter64片各8点、角primitive各8点；
241个径点、128个角点，未做连续余项证书。准确S与float末标签仍须最终按真实定义覆盖。

| 中央实际gap | sampled相对metric最大值 | sampled角向相对误差 | sampled主曲率最大值 |
|---|---:|---:|---:|
| 0 | 3.49e−15 | 8.89e−16 | 6.96902 |
| .05 | .1327004146 | 8.89e−16 | 7.00643 |
| .64 | 2.5695923205 | 8.89e−16 | 35.1852 |
| .9 | 4.1664222543 | 8.89e−16 | 243.459 |

所有采样Gram行列式为正，但这不是连续浸入或嵌入证明。
gap .64/.9的明显曲率与metric缺陷如实保留；没有把中央强幅度误报完整强解。
四个初值的真实中央/cut数值metric都约机器舍入，仅说明所定义边界实现。

实际完整报告：
`notes/2026-11-12-fd2d-direct-position-tangent-lift-R187-01-report.json`，
5741B，SHA256 `fb5a5c84ff39153cbf3c537c97ac8383cd654aa3621b39ba877d3744d338a23c`，
已main dad9ad76f8cd82e1c62141307cee4e0c831e91f2。
以后需要重做可用Node CLI，另选输出名：
~~~sh
node scripts/fd2d-direct-position-tangent-lift-baseline-R187.cjs \
 notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json \
 notes/R187-new-actual-report.json
~~~
原kernel已保存，不为额外流程重复执行。下一直接实现完整两角/位置残差的有限非线性方向和真实试步；它是独立候选，强目标仍未完成。
