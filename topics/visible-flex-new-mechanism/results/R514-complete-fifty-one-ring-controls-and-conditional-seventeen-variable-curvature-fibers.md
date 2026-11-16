# R514：真实58末三样条的完整51控制、实际形算子与条件17维曲率纤维

2026-11-16。本文只作原源码和已发表结果的纸面推导，没有执行几何、参数J、求积、符号程序、rank、求解器或开发检查。本文证明独立于ring17的数值结果；其已完成的无候选观察见[原记录](../notes/true58-ring17-original-box-LP-infeasible-return-no-candidate-20261116.md)。下面不把数值返回用作数学前提，也不向已闭任务添加调用。

**主结论。** 原末三条径向样条给每个原角模式独立的值、一阶径向jet、二阶径向jet。其完整51维有限族有一个准确的三层结构：值层决定整圈位置和角切向量；一阶层决定真实第一形式、法向及形算子第二列；固定前两层后，最高径向jet的17个共同系数只让形算子第一个对角元仿射变化。原172物理盒同时约束三层，不能拆成三个独立参数盒。于是完整环控制可准确缩成34个非线性低阶状态加一个条件17维线性可行问题，而不是无结构的51维搜索；全body约束仍含中段真实非线性交互。

## 1. 唯一当前点、原来源和本文的覆盖范围

当前点取[原两网实际接受的58](../notes/true57-nonlinear168-original-two-grid-accepted58-20261116.md)，其physical SHA256为

$$
\mathtt{94950b2bd5d7b5241e14333a4315b073f64840f74849a7909d6de8cb3cc29f54}.
$$

该原收据的细网曲率峰在 $s=.78,\theta=4.818744981678094$，并非反射轴；本文没有使用轴上主曲率分离。两主曲率的原排序也不被解释成径向、角向标签。固定 $g,b_0$、完整168场、原172盒和永久参考均保持同一来源。

数学依据为：

- [R510](R510-original-three-spline-ring-metric-neutrality-and-affine-axis-curvature-control.md) 的原三样条全区延拓；
- [R511](R511-complete-ring-curvature-intervals-and-shared-seventeen-coefficient-control.md) 的共同17系数和完整形算子区间；
- [R504](R504-complete-168-parameter-line-second-metric-jets-and-curvature-PSD-remainders.md) 的完整有限场、全角 $\Pi$ 及二阶链式；
- [完整168场](../scripts/frame_complete_body_extension168.py)、[原frame](../scripts/frame_collar_bvp.py)、[原角列和结点](../scripts/frame_collar_enriched.py)、[原entry权](../scripts/frame_entry_paired_repair.py)；
- [原实际曲率](../scripts/frame_curvature_psd.py) 和 [原mirror公式](../scripts/frame_metric_epigraph_dense.py)。

只有原 $u$ 的 $9\times9=81$ 个系数及原 $v$ 的 $9\times8=72$ 个系数在本文讨论的153维前后块中变化。单Q、五个null-height及新增九个坐标在增量中为零，其在真实58中已有的非零值照常进入背景场。本文的51维族不是把当前完整场退回旧159点，也不是重新建立一个不同的 $g$。

固定原径向行 $\sigma\in(153/200,423/500)$。记 $b=423/500$。符号 $.78$ 是位置标签：若程序以原binary64径向行建造嵌入，应取该同一binary64数的精确有理值作 $\sigma$；若数学上取 $39/50$，也必须始终使用该同一个值。不能在求三jet组合时用一个 $\sigma$，再以另一个舍入值宣称两个零jet准确成立。

## 2. 三个完整Hermite组合与51个真实坐标

令 $\mathcal B_9,\mathcal B_{10},\mathcal B_{11}$ 为原全结点向量中的三条自由五次样条。R510已付其在最后结点片上的三jet映射可逆。令

$$
y=s-\sigma,\qquad d=b-\sigma>0.
$$

在最后结点片，三个标准组合为

$$
\begin{aligned}
R_0(s)&=\left(\frac{b-s}{d}\right)^3
 \left(1+\frac{3y}{d}+\frac{6y^2}{d^2}\right),\\
R_1(s)&=\left(\frac{b-s}{d}\right)^3
 \left(y+\frac{3y^2}{d}\right),\\
R_2(s)&=\left(\frac{b-s}{d}\right)^3\frac{y^2}{2}.
\end{aligned}
\tag{1}
$$

它们满足

$$
R_k^{(j)}(\sigma)=\delta_{jk},\qquad j,k=0,1,2.
\tag{2}
$$

每一个 $R_k$ 必须以唯一原样条系数作全区延拓：

$$
R_k(s)=\sum_{\ell=0}^2 W_{\ell k}\mathcal B_{9+\ell}(s),
\qquad
W=\left[\mathcal B_{9+\ell}^{(j)}(\sigma)\right]_{j,\ell=0}^2{}^{-1}.
\tag{3}
$$

式(1)只描述末片；不能在 $.765$ 截断。原三支持的并集从 $.36$ 开始，entry权在此前已恒为1，所以(3)在真实原 $u/v$ 系数中成立，不是去掉entry权后得到的另一族。其余片段仍是原样条，保持原接口正则性；不额外宣称原有限表示变成全局 $C^\infty$。

记原角列为

$$
\boldsymbol a(\theta)=(a_1,\ldots,a_9),\qquad
\boldsymbol d(\theta)=(d_1,\ldots,d_8).
$$

其中保留原theta模、真实phi模和原core列及其顺序，不以一个新的正弦拟合替换它们。对 $k=0,1,2$ 选共同系数

$$
x_k=(x_k^u,x_k^v)\in\mathbb R^9\times\mathbb R^8,
\quad
A_k(\theta)=\boldsymbol a(\theta)\cdot x_k^u,
\quad
D_k(\theta)=\boldsymbol d(\theta)\cdot x_k^v.
\tag{4}
$$

完整后段控制为

$$
\Delta u=\sum_{k=0}^2R_kA_k,\qquad
\Delta v=\sum_{k=0}^2R_kD_k,\qquad
\Delta z=\Delta b=0.
\tag{5}
$$

$W$ 可逆说明这51个数与原末三个径向位置的51个 $u/v$ 系数一一对应。这是原三jet映射的代数结论，不是新执行的网格rank观察。每个角点仍使用同一组 $x_0,x_1,x_2$，没有逐角自由选择51个不同向量。

## 3. 全body的完整有限场和位置一、二jets

令 $u_*,v_*,z_*,b_*=z_*'$ 是当前58的完整场，包含冻结的新九和null-height背景。先不加前102列。对任意有限 $(x_0,x_1,x_2)$，把(5)直接代入

$$
u=u_*+\Delta u,\qquad v=v_*+\Delta v,\qquad
\psi=\theta+u,\quad c=(1+v^2)^{-1/2},
$$

$$
N=(\cos\psi,\sin\psi,0),\qquad
H=(-\sin\psi,\cos\psi,0),\qquad
T=cH+vc\,e_3.
\tag{6}
$$

这保留全部相位和真实 $c(v)$，不是关于 $x_0$ 的Taylor模型。原角对称和闭合由相同原字段族继承；$\Pi$仍是同一个完整角圈上的零均值原函数。

原frame的必要偏导为

$$
\begin{aligned}
T_u&=-cN,&T_v&=c^3(e_3-vH),\\
T_{uu}&=-cH,&T_{uv}&=vc^3N,\\
T_{vv}&=(2v^2-1)c^5H-3vc^5e_3.
\end{aligned}
\tag{7}
$$

因此在全部径向位置，

$$
\begin{aligned}
T_s&=T_u u_s+T_v\,v_s,\\
T_{ss}&=T_u u_{ss}+T_v\,v_{ss}
       +T_{uu}u_s^2+2T_{uv}u_sv_s+T_{vv}v_s^2,\\
T_\theta&=T_u(1+u_\theta)+T_v\,v_\theta.
\end{aligned}
\tag{8}
$$

这里 $T_v\,v_s$ 是一阶frame偏导与标量径向导数的乘积，$T_{vv}$才是二阶frame偏导。式(8)中的 $\theta+u$ 必须保留那个1。

固定 $a(s)$ 和完整高度函数后，真实位置全部一、二jets为

$$
\begin{aligned}
X&=a\Pi T+z_*e_3,\\
X_s=U&=a_s\Pi T+a\Pi T_s+b_*e_3,\\
X_\theta&=aT,\\
X_{ss}=Z_{11}&=a_{ss}\Pi T+2a_s\Pi T_s+a\Pi T_{ss}+b_{*,s}e_3,\\
X_{s\theta}&=a_sT+aT_s,\\
X_{\theta\theta}&=aT_\theta.
\end{aligned}
\tag{9}
$$

各 $\Pi$ 作用完整角函数，不能从单轴值或某个角点的局部frame反推出。$z_*$ 的原锚和 $b_*,b_{*,s}$ 均保留；固定的是高度坐标，不意味着 $X$ 的第三分量在一般 $R_0$ 变化下保持不变。

若已有完整背景 jets，可用差式

$$
\begin{aligned}
X-X_*&=a\Pi\Delta T,\\
U-U_*&=a_s\Pi\Delta T+a\Pi\Delta T_s,\\
Z_{11}-Z_{11,*}
 &=a_{ss}\Pi\Delta T+2a_s\Pi\Delta T_s+a\Pi\Delta T_{ss},\\
X_{s\theta}-X_{s\theta,*}&=a_s\Delta T+a\Delta T_s,\\
X_{\theta\theta}-X_{\theta\theta,*}&=a\Delta T_\theta.
\end{aligned}
\tag{10}
$$

式(10)不需要另积分一个tangent-dependent center，但未存的 $X_*,Z_{11,*}$不能因此被当成已经付费或补成零。只存 $U/T$ 时，真正缺失的固定高度导数或原位置输入仍须按其来源恢复。

## 4. 选定整圈上的准确三层结构

以下所有背景量在 $s=\sigma$ 取值。由(2)，令

$$
\widehat u=u_*+A_0,\qquad \widehat v=v_*+D_0,\qquad
p=u_{*,s}+A_1,\qquad r=v_{*,s}+D_1.
\tag{11}
$$

式(7)的全部偏导现在必须在 $(\widehat u,\widehat v)$ 求值。整圈有

$$
\begin{aligned}
T&=T(\widehat u,\widehat v),\\
T_s&=T_up+T_vr,\\
T_\theta&=T_u(1+u_{*,\theta}+A_{0,\theta})
          +T_v(v_{*,\theta}+D_{0,\theta}),\\
T_{ss}&=T_u(u_{*,ss}+A_2)+T_v(v_{*,ss}+D_2)
         +T_{uu}p^2+2T_{uv}pr+T_{vv}r^2.
\end{aligned}
\tag{12}
$$

这立即给下表。表中的“独立”只指本圈对该组参数的准确独立，不是全body或浮点逐位声明。

| 本圈真实量 | 依赖的控制层 |
|---|---|
| $T,T_\theta,X,X_\theta,X_{\theta\theta}$ | 仅 $x_0$ |
| $T_s,U,X_{s\theta}$ | $x_0,x_1$；固定 $x_0$ 后对 $x_1$ 仿射 |
| 第一形式、法向、面积及mirror | $x_0,x_1$，一般非线性 |
| $T_{ss},X_{ss}$ | $x_0,x_1,x_2$；固定前两层后对 $x_2$ 仿射 |
| 位置型signed-height/ball/strip在本圈的输入 | 仅 $x_0$ |
| 整个body的原14门 | 一般同时依赖全部三层，不能由本表代替 |

原mirror实际多项式是
$X_3^2|U\times T|^2-\tau_m^2(U\times T)_3^2$；
因此它确在本圈独立于 $x_2$，但随 $x_1$ 的法向变化而变，不能归入只依赖位置的第一层。

## 5. $R_1$ 的二次项与真实法向变化不能删除

固定 $x_0$，记 $p_*=u_{*,s},r_*=v_{*,s}$。从 $x_1=0$ 到一般 $x_1$，(12)的完整变化为

$$
\Delta_{1}T_s=T_uA_1+T_vD_1,
\tag{13}
$$

$$
\begin{aligned}
\Delta_{1}T_{ss}
={}&2(T_{uu}p_*+T_{uv}r_*)A_1
 +2(T_{uv}p_*+T_{vv}r_*)D_1\\
 &+T_{uu}A_1^2+2T_{uv}A_1D_1+T_{vv}D_1^2.
\end{aligned}
\tag{14}
$$

最高径向控制再准确添加 $T_uA_2+T_vD_2$。式(14)的平方及交叉项不能因为 $R_1(\sigma)=R_1''(\sigma)=0$ 而删除；它们来自原frame对标量场的非线性链式。

固定 $x_0$ 后，记

$$
V=a\Pi(T_uA_1+T_vD_1).
$$

有 $U=U_0+V$、$T=T_0$，于是

$$
w=U\times T=w_0+V\times T,\qquad n=\frac{w}{|w|}.
\tag{15}
$$

所以 $R_1$ 虽然保持 $T_\theta$，仍能通过 $U$、法向和正交化改变角向与混合曲率。不能把“保持 $T_\theta$”误说成“保持形算子第二列”。是否在当前58原17个角模式中具有所需非零耦合，是后续真实系数问题；本文没有代入计算该耦合。

式(12)–(14)的链式及固定前四槽后的最高jet线性结构已由另一代理作窄纸面独核；该范围不扩展到当前系数、物理盒可行性或实际门通过。

## 6. 保留实际 $G$ 的完整形算子

为与原 curvature_values 一致，定义原归一二jet

$$
Z_{12}=\frac{X_{s\theta}}a=\frac{a_s}aT+T_s,
\qquad
Z_{22}=\frac{X_{\theta\theta}}{a^2}=\frac{T_\theta}a.
\tag{16}
$$

令

$$
E=U\cdot U,\quad F=U\cdot T,\quad G=T\cdot T>0,
\quad q=|U\times T|>0,\quad n=\frac{U\times T}{q},
$$

$$
L=n\cdot Z_{11},\qquad M=n\cdot Z_{12},\qquad N_c=n\cdot Z_{22}.
\tag{17}
$$

连续精确frame满足 $G=1$，但以下一般式不需要把它代成1。设

$$
d=E-\frac{F^2}{G}>0,\qquad t=\frac FG.
$$

在真实正交基

$$
\left(\frac{U-tT}{\sqrt d},\frac{T}{\sqrt G}\right)
$$

中，形算子准确为

$$
S=\begin{pmatrix}A&B\\B&C\end{pmatrix},
\quad
\boxed{
 A=\frac{L-2tM+t^2N_c}{d},\quad
 B=\frac{M-tN_c}{\sqrt{dG}},\quad
 C=\frac{N_c}{G}.
}
\tag{18}
$$

(18)适用于58的非轴峰，保全部混合项。原矩阵等价写成

$$
I=\begin{pmatrix}E&F\\F&G\end{pmatrix},\qquad
\mathcal K=q\begin{pmatrix}L&M\\M&N_c\end{pmatrix},
\quad qI\pm K^{-1}\mathcal K\succeq0.
\tag{19}
$$

固定曲率目标 $K>0$ 时，(19)等价于 $K I_2\pm S\succeq0$，这里 $I_2$ 是二维单位矩阵。原代码的四trace/determinant行及其原尺度可以沿(19)使用；不能把第一基本形式 $I$当成单位阵。

数值实现应从同一已绑定实际 $X_s,X_\theta/a$ 和原曲率数组读取 $E,F,G,q,I,II$。原二进制运算中 $G-1$、$q^2-(EG-F^2)$可能有舍入差；需保其真实值和新求值身份，不能用数学单位长度消去实际字段或声称无舍入误差。

## 7. 固定低阶34参数后，仍是准确的共同17维曲率纤维

固定 $x_0,x_1$ 且保持 $q>0$。把 $x_2=0$ 的形算子记为 $S^{01}$，其分量为 $A^{01},B^{01},C^{01}$。定义

$$
\begin{aligned}
\ell_i^u(x_0,x_1;\theta)&=
 \frac{a\,n\cdot\Pi(T_u a_i)}{d},\\
\ell_j^v(x_0,x_1;\theta)&=
 \frac{a\,n\cdot\Pi(T_v d_j)}{d}.
\end{aligned}
\tag{20}
$$

则整个有限51族在该固定低阶纤维上满足

$$
\boxed{
 S(x_0,x_1,x_2;\theta)=
 \begin{pmatrix}
 A^{01}+\ell^{01}(\theta)\cdot x_2&B^{01}\\
 B^{01}&C^{01}
 \end{pmatrix}.
}
\tag{21}
$$

证明：由(12)，$T,T_s,T_\theta$均独立于 $x_2$，故(9)、(17)中的 $I,q,n,M,N_c$固定；只有
$\Delta L=a\,n\cdot\Pi(T_uA_2+T_vD_2)$。代(18)即得(21)。

这不是在 $x_2=0$ 附近的一阶近似，因而不要求 $x_2$小；但(20)必须在当前 $(x_0,x_1)$重建，不能把原58的 $\ell$跨低阶状态搬来当同一个模型。整个共同17系数仍同时服务两网所有角点。

直接使用(19)也能看到相同线性性：只有 $\mathcal K_{11}$随 $x_2$线性改变，其余三项固定，所以两trace和两determinant都是 $x_2$的仿射函数。无须把一个通常非线性的全51曲率函数冒称线性。

令 $a_0=A^{01},B=B^{01},C=C^{01},z=\ell^{01}\cdot x_2$。可完整保四行

$$
\begin{aligned}
2K+a_0+C+z&\ge0,\\
(K+C)(K+a_0+z)-B^2&\ge0,\\
2K-a_0-C-z&\ge0,\\
(K-C)(K-a_0-z)-B^2&\ge0.
\end{aligned}
\tag{22}
$$

这些行对 $z$仿射，且不除以 $K\pm C$，保留边界分支。在 $|C|<K$时，等价区间为

$$
-K-a_0+\frac{B^2}{K+C}
 \le z\le
K-a_0-\frac{B^2}{K-C}.
\tag{23}
$$

$|C|>K$，或 $|C|=K,B\ne0$，则该纤维在该点不可行；$|C|=K,B=0$时保 $-K-a_0\le z\le K-a_0$；$\ell=0$时保原常数行。这些仍是准确实数分支，不用小正数替代真实零分母。

## 8. 原172盒怎样同时约束三层

对每个原角模式 $j$，把其三个末径向物理系数增量记为 $\delta c_{\ell j}$。由(3)有

$$
\delta c_{\ell j}=\sum_{k=0}^2W_{\ell k}x_{kj},
\qquad \ell=0,1,2.
\tag{24}
$$

对 $u$ 和 $v$均用同一个真实 $W$，但保各自原物理系数的盒上下界。其余121个物理坐标在51族中固定。若原盒为 $[\underline c,\overline c]$，原58物理点为 $c_*$，则

$$
\underline c_{\ell j}-c_{*,\ell j}
 \le\sum_kW_{\ell k}x_{kj}
 \le\overline c_{\ell j}-c_{*,\ell j}.
\tag{25}
$$

新规范若取 $h=4\|M\Delta q\|_\infty$，则在本51族中

$$
-h/4\le\sum_kW_{\ell k}x_{kj}\le h/4.
\tag{26}
$$

$M$仍是原172×168映射；本族全在其原切向恒等块中，不能用只看 $x_k$的任意norm代替(26)。$h$可作新的epigraph变量并以 $\min h$为目标；不默认承继旧 $1/128$作为未来全51研究限制。任何具体上限须另由新任务声明。

固定 $x_0,x_1,h$时，令

$$
o_{\ell j}=W_{\ell0}x_{0j}+W_{\ell1}x_{1j},
$$

$$
l_{\ell j}(h)=
 \max\{\underline c_{\ell j}-c_{*,\ell j},-h/4\},\quad
u_{\ell j}(h)=
 \min\{\overline c_{\ell j}-c_{*,\ell j},h/4\}.
\tag{27}
$$

每条物理约束准确变成

$$
l_{\ell j}(h)-o_{\ell j}
 \le W_{\ell2}x_{2j}
 \le u_{\ell j}(h)-o_{\ell j}.
\tag{28}
$$

若 $W_{\ell2}>0$直接除，若为负则交换两端；若为零则检查原常数不等式。三条交集给该角模式的闭区间 $[L_j,U_j]$，为空即排除这个低阶状态及 $h$。因此，在加入曲率耦合前，最高17维的原盒域准确是这些区间的直积；加入(22)后仍是一个共同线性多面体。

这说明原盒不能变成“分别允许 $x_0,x_1,x_2$各自移动同样幅度”的三个盒。三个径向jet会在同一物理系数里相加，允许的幅度可以显著耦合，也可能只剩单侧。

## 9. 一个比无结构51维搜索更具体的等价缩减

固定连续完整角圈或明确的原粗、细两角网 $\Theta$，固定目标 $K$和原物理盒。给 $(x_0,x_1)$定义：

1. 用(6)、(9)、(12)取得真实低阶环态；
2. 检查需要的本圈位置、原metric、mirror和regularity门；
3. 取满足(22)、(25)、(26)及声明的 $h$范围的共同 $(x_2,h)$集合，记为 $\mathcal P_K(x_0,x_1)$。

其中第2项的所有输入在本圈独立于 $x_2$；第3项在有限 $\Theta$上是18变量线性约束，其中17个真实控制加一个norm epigraph。若不用 $h$变量，则是17变量条件可行问题。

**等价定理。** 在所选角集合上，原51族满足这些本圈门、目标曲率和原盒，当且仅当存在一个真实低阶状态 $(x_0,x_1)$满足第2项且

$$
\mathcal P_K(x_0,x_1)\ne\varnothing.
\tag{29}
$$

证明的正向是取原参数的前两层和第三层，用(21)、(24)逐项代入；反向由 $W$可逆将同一三层参数还原为原51系数，(6)–(12)给真实有限场，(22)和物理行分别给所声明的本圈曲率与盒门。没有删除尾片、中段、角原函数或高度基线。

因此可以先研究一个34维真实低阶像，再在每个低阶状态上精确处理共同17维线性纤维，而不必把51个变量一概交给一般非线性搜索。不过(29)没有免费求解外层，也不证明任何当前低阶状态可行；每个真正新内层solver或低阶评价都须在未来独立账户收费。

若 $\Theta$为连续角圈，第三项是具有同样17个未知数的半无限线性系统；只检查原两有限网不能升级为连续所有角点。若加入整个body的14门，则中段对 $x_2$也非线性，不能继续把整个任务称为此线性纤维。

## 10. 三条可以在低阶层严格使用的必要条件

### 10.1 不可变列门属于每一个低阶纤维

由(21)，对任何 $x_2$，

$$
\|S\|_{\rm op}\ge\sqrt{(B^{01})^2+(C^{01})^2}.
\tag{30}
$$

所以任一角点该下界超过 $K$，就排除**这个固定** $(x_0,x_1)$的全部二阶控制。它不排其它 $R_0/R_1$状态，也不排完整168族。特别地，原ring17只是 $(x_0,x_1)=(0,0)$这一纤维。

### 10.2 原metric门可写成低阶二次条件，但不是全部凸

原实际metric量仍是

$$
e=E-1,\qquad f=F,\qquad
\eta=\frac{|e|+\sqrt{e^2+4f^2}}2.
$$

没有为数值 $G-1$另造一条原metric门。对任意明确 $\varepsilon\in(0,1)$，准确等价为

$$
\boxed{
 \eta\le\varepsilon
 \quad\Longleftrightarrow\quad
 E+\frac{F^2}{\varepsilon}\le1+\varepsilon,\qquad
 E-\frac{F^2}{\varepsilon}\ge1-\varepsilon.
}
\tag{31}
$$

证明是分别令 $\varepsilon I_2\pm
\begin{psmallmatrix}e&f\\f&0\end{psmallmatrix}$为PSD，并用其右下角 $\varepsilon>0$取Schur补。

固定 $x_0$ 后 $U$对 $x_1$仿射、$T$固定，故(31)是完整的二次条件。第一条为凸二次上界；第二条一般不是凸可行集，不能因为第一条是椭球型就宣整个metric低阶域凸。

当 $G\ge\varepsilon$时，第二条还给

$$
E-\frac{F^2}{G}
 \ge1-\varepsilon+
     \left(\frac1\varepsilon-\frac1G\right)F^2
 \ge1-\varepsilon,
\quad
q^2\ge G(1-\varepsilon).
\tag{32}
$$

这是准确一致输入下的面积下界。实际程序仍保独立normal-area门及原浮点容差，不由(32)删除原检查。

由于全body最大 $\eta$不小于本圈最大 $\eta$，若新任务要求相对58下降至少 $\delta_\eta>0$，则

$$
\max_{\theta\in\Theta}\eta(x_0,x_1;\sigma,\theta)
 \le \eta_{58,\mathrm{source}}-\delta_\eta
\tag{33}
$$

是该任务在同一角集合上的必要条件。任何 $x_2$和任何前102列均不能改变它。当前58已付的metric峰在 $.4725$，不是本圈 $.78$；本文没有计算(33)的当前余量，也不把该峰位置当作(33)已经满足的数值证明。

### 10.3 有限 $R_1$ 法向旋转不足时的必要障碍

固定 $x_0$，设参考 $x_1=0$规则，$q_0>0$，并在一个由原盒导出的允许 $x_1$域中有真实界 $|V(\theta)|\le D(\theta)$，其中 $V$如(15)。对任一仍规则的候选，

$$
|n-n_0|\le\frac{2|V\times T|}{q_0}
          \le\frac{2\sqrt G\,D}{q_0}.
$$

因此

$$
\boxed{
 |C(x_1)-C(0)|
 \le\frac{2|T_\theta|D}{a\sqrt G\,q_0}.
}
\tag{34}
$$

若某点满足

$$
|C(0)|-\frac{2|T_\theta|D}{a\sqrt G\,q_0}>K,
\tag{35}
$$

则这一固定 $x_0$、整个受限 $x_1$域和所有 $x_2$均不能达到目标；需要改变 $R_0$或扩大真正的允许域，而不是继续同一二阶族。

这里 $D$不能凭经验取值。一个明确但可能保守的来源是原盒对
$x_{1j}=\sum_\ell\mathcal B_{9+\ell}'(\sigma)\delta c_{\ell j}$
给出的界。记由此得到的允许一阶系数集为 $\mathcal D_1$，可取统一角界

$$
\overline D=
 a\|\Pi\|_{\infty\to\infty}
 \sup_{x_1\in\mathcal D_1}
 \left(\|cA_1\|_\infty+\|c^2D_1\|_\infty\right),
\qquad |V(\theta)|\le\overline D.
\tag{36}
$$

于是(34)–(35)可以取 $D(\theta)=\overline D$，或使用另有真实证明的更细逐点界。这里 $|T_u|=c$、$|T_v|=c^2$。完整原角函数和原 $\Pi$范数仍保留，可用R504的连续或相应固定离散算子界。若(35)不给严格正差，只是这个充分排除未成立；本文没有计算当前58的 $D$或据此预判ring17。

## 11. 前102列的真实作用与不可删除的中段耦合

原前六径向自由列 $\mathcal B_3,\ldots,\mathcal B_8$配同17角模式给102个系数。它们连同原entry权的支持右端至多为 $.765$，因此在 $\sigma$的一个开邻域中，全部标量值与必要空间jets准确为零。

令前组嵌入为 $\mathsf Fz$，末51嵌入为 $\mathsf E(x_0,x_1,x_2)$。在本圈，

$$
J^2X(q_{58}+\mathsf E x+\mathsf Fz)
 =J^2X(q_{58}+\mathsf E x),
\tag{37}
$$

此处 $J^2X$含原位置及全部一、二jets。固定的高度函数保证没有一个被漏掉的tangent前缀center从前段传播到本圈。

两组占据不同原物理切向系数，故

$$
\|M(\mathsf E x+\mathsf Fz)\|_\infty
=\max\{\|M\mathsf E x\|_\infty,\|M\mathsf Fz\|_\infty\},
\tag{38}
$$

逐坐标原盒也相应分开。然而，末三样条的支持从 $.36$开始，与前六列在中段相交；那里(37)不成立。

更准确地，若两组标量增量分别为 $l=(\Delta u_l,\Delta v_l)$、
$f=(\Delta u_f,\Delta v_f)$，则有限的frame混合差是

$$
\begin{aligned}
&T(u_*+l_u+f_u,v_*+l_v+f_v)
 -T(u_*+l_u,v_*+l_v)\\
&\qquad
 -T(u_*+f_u,v_*+f_v)+T(u_*,v_*)\\
&=\int_0^1\!\!\int_0^1
 D^2T(u_*+\alpha l_u+\beta f_u,
       v_*+\alpha l_v+\beta f_v)[l,f]\,d\alpha\,d\beta.
\end{aligned}
\tag{39}
$$

其中完整二次双线性型为

$$
D^2T[l,f]
 =T_{uu}l_uf_u+
   T_{uv}(l_uf_v+l_vf_u)+T_{vv}l_vf_v.
\tag{40}
$$

各偏导在积分中的真实有限状态求值，不是只取基点的一个二阶近似。把(39)及其径向导数沿(9)送入完整 $\Pi$，就得到全部位置一、二jets的真实混合项。

因此，前102列确能在不动本圈的条件下改变较前body，但不能免费修复末51在中段造成的一切metric、mirror或curvature变化。全身仍必须是同一个最终候选、同一完整非线性预测和原两网14门。式(38)只说明物理系数norm/盒的分块，不说明几何约束分块。

## 12. 精确参数族、实际舍入和付费输入

式(1)–(40)首先是同一个实数/有理系数族的恒等。给定求解器返回的二进制 $\xi$，可以把它作为精确有理数，经同一个 $W$生成未舍入原168/172增量，再逐坐标得到实际binary64候选。

独立舍入会改变三jet的精确关系。因此必须分别保：

- 三组求解系数及精确 $W$；
- 未舍入的完整168/172增量、原物理 $h$与盒判定；
- 实际rounded168/172、精确舍入差及其真实盒/范数判定；
- 实际候选重新取得的scalar/frame、两网metric与curvature预测身份；
- 最终原ordinary的两网14门及严格eta下降。

浮点条件LP行通过仅说明它的数值模型残差，不自动证明rounded候选仍位于原精确jet纤维，也不授权省掉全body预测。

原58 CACHE2含完整 $U/T/e/f$和按原pool导出的selected二jets；selected不是完整圈。构造任一新的低阶环态需要真实当前标量场、完整角列、固定 $a,a_s,a_{ss}$、必要高度 $b_*,b_{*,s}$，以及位置门所需的真实 $z_*$或已付 $X$。没有保存的二jets不能补零，旧58的 $\ell$也不能跨 $(x_0,x_1)$冒作新绑定。

已发布的metric/curvature predictor可按原式提供新的必要数组，且不要求ordinary的center查询；但它们仍是有成本的新预测，不是缓存已付宣言。相同原角网/相同 $\Pi_N$保持上述代数层次；连续全角与浮点求值仍分别说明，不能由有限节点通过授予连续reach。

本文没有实现或执行全51求解器，没有决定新的外层次数/预算，也没有利用已闭ring17任务的余额。root后续若选择这一机制，应按真正新低阶状态、条件问题、全body预测和actual分别记账，原所有封存费用原样保留。

## 13. 本稿闭合的结论

本稿付清了原51系数与三个径向jet层的精确对应、全部有限 $X$一/二jets、$R_1$不可删除的平方和法向变化、保实际 $G$的一般形算子、固定34低阶参数后的共同17维曲率线性纤维、三层同时受约束的原172盒，以及前102列准确不动峰环而中段仍完整耦合的事实。

新可用缩减是(29)，新必要门包括(30)、原metric二次条件(31)、全body下降所需的本圈门(33)，以及在有真实幅度界时可使用的法向旋转障碍(35)。它们均没有证明当前58存在所需可行控制，也没有证明完整168或一般固定 $g$问题不可能。ring17原观察已另记其无候选返回，不能代替准确不可行证明；全51的原盒可行性、连续全角/全body及非局部reach仍待各自真实支付。
