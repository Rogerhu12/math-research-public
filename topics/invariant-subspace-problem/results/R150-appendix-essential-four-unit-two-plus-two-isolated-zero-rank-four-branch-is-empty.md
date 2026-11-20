# R150 附录：孤立零点加两个单位双点的 rank-four 支路全部为空

作者：Astra-ISP-b2a9acde-20261120（root 与 r150_structure）；AI-assisted GPT-6 Astra Pro。日期：2026-11-20 UTC。状态：本条明确范围已证明。

第 5 节的实际有理乘子已逐项通过全部 325 个原系数等式，全部边界另由独立原源精确核验；完整运行身份与源见第 7 节。

## 1. 精确范围与统一原源

沿用[外均值 essential-four 长度五代数定理](R150-appendix-essential-four-outer-mean-length-five-algebra-and-rank-defects.md)的全部假设与物理坐标：
$$
 \operatorname{rank}\operatorname{Cat}_{3\times4}(y)=3,\qquad
 \dim\operatorname{ess}(T_3)=4,\qquad y\notin\operatorname{ess}(T_3).
$$
本支的原长度五支撑为两个活跃双点与一个不同的约化零点，
$L$ 在两个双点上为单位，在最后一点为零。以同一原 $L$ 归一单位因子，
$$
 B=\mathbb C[\epsilon]/(\epsilon^2)\oplus
   \mathbb C[\eta]/(\eta^2),\qquad
 \tau(x_0,x_1,x_2,x_3)=a x_0+x_1+b x_2+x_3,
$$
其中
$$
 a+b=1,\qquad \delta=a-b.
$$
最高 Frobenius 系数均非零，故允许分别缩放局部参数归一为一。
允许 $a=0$ 或 $b=0$；它们不破坏 Frobenius 配对非退化。
物理向量仍是同一原曲线点和其一阶 jets 的允许可逆变换。

记活跃极坐标为 $(X,Y,Z,T)$，零点极坐标为 $R$。
原矩给
$$
 T_3=P+R^3,
$$
$$
 P=S^3-3DSQ-\frac{3\delta}{2}D^2Q-\frac{ab\delta}{2}D^3,
 \quad D=X-Z,\quad S=Y+T,\quad Q=bY-aT.                     \tag{1.1}
$$
活跃原 Gram 矩阵、零点交叉列为
$$
 K_B=
 \begin{pmatrix}
 0&0&A&B\\
 0&C&D&E\\
 A&D&0&0\\
 B&E&0&G
 \end{pmatrix},\qquad U=(u,v,z,w)^T,                         \tag{1.2}
$$
其中矩阵字母 $D$ 与 (1.1) 临时的线性式 $D=X-Z$ 只在各自式内使用。
设
$$
 m=a u+v+b z+w,\qquad
 \widehat K=\begin{pmatrix}K_B&U\\U^T&0\end{pmatrix}.
$$
原长度五 jets 独立、原六维 $K$ 非退化，故
$$
 \operatorname{rank}\widehat K\ge4.                         \tag{1.3}
$$

下述统一公式都来自原完整梯度，不是另造的方程。
令 $D_Kx$ 的第 $i$ 分量为
$\tau((K_B)_{i,\bullet}x)$，乘法为两个双数因子的逐因子乘法；
令 $d=D_K1,\ \phi=\tau d/2$。原活跃 mean 是
$$
 e-2D_Kd-2d^2+4\phi d=0,                                   \tag{1.4}
$$
$$
 e=(\tau k_0^2,\ 2\tau k_0k_1,\ \tau k_2^2,\ 2\tau k_2k_3),
$$
其中 $k_i$ 为 $K_B$ 第 $i$ 行。原二次低梯度为
$$
 N=N_B+mR^2,\qquad
 N_B(x)=\tfrac12\tau((d-\phi)x^2)
 -(\tau x)\tau(dx)+\phi(\tau x)^2+\tfrac14\tau(xD_Kx).        \tag{1.5}
$$

设
$$
 p=P(K_Bu_0),\quad p_1=\partial_{K_Bu_1}P(K_Bu_0),\quad
 q=P(K_Bv_0),\quad q_1=\partial_{K_Bv_1}P(K_Bv_0),
$$
$$
 n=N_B(K_Bu_0),\quad n_1=\partial_{K_Bu_1}N_B(K_Bu_0),\quad
 o=N_B(K_Bv_0),\quad o_1=\partial_{K_Bv_1}N_B(K_Bv_0).
$$
原 highest 与 $N$ 在两个物理双点的值、jet 给
$$
 p=-u^3,\ p_1=-3u^2v,\ q=-z^3,\ q_1=-3z^2w,
$$
$$
 n=-mu^2,\ n_1=-2muv,\ o=-mz^2,\ o_1=-2mzw.                \tag{1.6}
$$
以下四个相容式因此没有任何非零除法限制：
$$
 c_a=3pn_1-2np_1=0,\qquad c_b=3qo_1-2oq_1=0,              \tag{1.7}
$$
$$
 \mu=3no-(3ap+p_1)o-(3bq+q_1)n=0,                         \tag{1.8}
$$
$$
 \chi=n^3q^2-o^3p^2=0.                                    \tag{1.9}
$$
(1.8) 直接代入等于
$3m u^2z^2(m-a u-v-bz-w)$，所以也适用于 $m=0,u=0,z=0$。
(1.9) 同样直接由 (1.6) 得到。没有在任何一处假定 $n,o,p,q$ 可逆。

半权 $\delta=0$ 的完整支路已经由
[单位双点半权附录](R150-appendix-essential-four-unit-two-plus-two-half-isolated-zero-rank-four-branch-is-empty.md)排除。
以下全部保留 $\delta\ne0$，并分清 $A$ 与 $B+D$ 的零值边界。

## 2. 完整边界一：$A=0$

若 $B=D=0$，(1.1)、(1.6) 给 $u=z=0$。
于是 $\widehat K$ 的两个基点方向的行列全为零，秩至多三，违反 (1.3)。

余下令
$$
 s=B+D,\qquad t_0=B-D,\qquad j=C+E,\quad k=G+E.
$$
原 mean 的第零、第二系数分别为
$$
 2B(j+k+\delta t_0),\qquad 2D(j+k+\delta t_0),
$$
所以 $j+k=-\delta t_0$。其余两系数的和与差为
$$
 -8jt_0+2\delta s t_0-4\delta t_0^2,\qquad
 4Et_0+2\delta t_0^2.                                      \tag{2.1}
$$

若 $t_0=0$，则 $B=D=\beta\ne0,\ k=-j$，而 $j,E$ 任意。
直接从 (1.1)、(1.5) 得
$$
 p=q=\beta^3,\quad n=o=0,\quad
 n_1=\beta^2(j-a\beta),\quad o_1=\beta^2(-j-b\beta).
$$
highest 迫 $u,z\ne0$，两个 $N$ 值迫 $m=0$，两个 $N$-jet 迫
$j=a\beta=-b\beta$。因 $a+b=1$，这与 $\beta\ne0$ 矛盾。

若 $t_0\ne0$，(2.1) 给出唯一的活跃 mean 形式
$$
 B=(s+t_0)/2,\quad D=(s-t_0)/2,\quad
 C=\delta s/4,\quad E=-\delta t_0/2,\quad G=-\delta s/4.       \tag{2.2}
$$
这里
$$
 p=B^3,\quad q=D^3,\quad n=\tfrac{t_0}{2}B^2,\quad
 o=-\tfrac{t_0}{2}D^2.
$$
若 $BD\ne0$，(1.9) 的左侧为
$$
 \chi=\frac{t_0^3}{4}B^6D^6\ne0,
$$
矛盾。若 $B=0$，则 $s=-t_0,\ D=-t_0$，由原值/jet
$$
 q=-t_0^3,\quad q_1=-3\delta t_0^3/4,\quad
 o=-t_0^3/2,\quad o_1=-\delta t_0^3/2,
$$
于是
$$
 c_b=3\delta t_0^6/4\ne0.
$$
$D=0$ 由交换两个原双点得到同一矛盾。故 $A=0$ 已全部排除，
包括 $s=0$、两种 Frobenius 权为零和所有 Gram 退化情况。

## 3. 完整边界二：$A\ne0,\ B+D=0$

所有原必要方程对同时缩放所有 Gram 配对齐次，因此令 $A=1$。
设 $t_0=B-D,\ h=j+k,\ \ell=j-k$。
原 mean 的第零、第二系数的和为 $\delta(t_0-\delta)$，
故 $t_0=\delta$；它们的差遂给 $\ell=0$。
剩余两个 mean 相同，给
$$
 B=\delta/2,\quad D=-\delta/2,\quad j=k=h/2,
$$
$$
 E=\frac{h(1-\delta^2-h)}2+\frac{\delta^2(1-\delta^2)}8,
 \qquad C=G=h/2-E.                                        \tag{3.1}
$$
令 $\rho=\delta^2+2h$。由 (1.1)、(1.5) 重建的两个 (1.7) 满足
$$
 c_a+c_b=-\frac{3\delta^2}{128}(\rho^2+\delta^2),\qquad
 c_a-c_b=\frac{3\delta}{64}\rho(\rho^2-\rho-\delta^2).           \tag{3.2}
$$
因 $\delta\ne0$，第一式迫 $\rho\ne0$。两式给
$$
 \rho=-2\delta^2,\qquad \delta^2=-1/4,\qquad \rho=1/2,\qquad h=3/8.
$$
在这两个候选上
$$
 p=\delta/8,\quad q=-\delta/8,\quad
 n=(1+2\delta)/64,\quad o=(1-2\delta)/64.
$$
但
$$
 n^3-o^3=\delta/32768\ne0,\qquad p^2=q^2=\delta^2/64\ne0,
$$
违反 (1.9)。所以这整个边界也为空，不需要假设任何零点极坐标非零。

## 4. 剩余 active mean 的完整二参数形式

现在
$$
 A(B+D)\delta\ne0.
$$
令 $A=1$，并定义
$$
 s=B+D\ne0,\qquad t_0=B-D,\qquad r=t_0-\delta,\qquad
 h=j+k,\quad \ell=j-k.
$$
原 mean 第零、第二系数的和与差恰为
$$
 -\delta^2+\delta t_0-\delta^2s+2\delta t_0s+2hs,              \tag{4.1}
$$
$$
 \delta^3-\delta s-3\delta^2t_0+2\delta t_0^2
   +2(t_0-\delta)h+2\ell.                                  \tag{4.2}
$$
因此
$$
 h=-\delta^2/2-\delta r-\delta r/(2s),\qquad
 \ell=\delta(s^2+r^2)/(2s).                                 \tag{4.3}
$$
把它们代入其余 mean，两个式之和唯一给
$$
 E=-\frac{\delta r}{2}+\frac{\delta r^3}{2s}
   -\frac{\delta r}{4s}-\frac{\delta^2}{8}
   -\frac{\delta^2r^2}{8s^2}.                               \tag{4.4}
$$
剩余条件恰为
$$
 s^3+s r^2-4s r^4+2\delta r^3=0.                            \tag{4.5}
$$
若 $r=0$，则 (4.5) 给 $s=0$，矛盾。故可设
$$
 t=s/r\ne0,\qquad
 \delta=\frac t2(4r^2-t^2-1)\ne0.                            \tag{4.6}
$$
最终完整形式为
$$
 B=\frac{r(t+1)+\delta}{2},\qquad
 D=\frac{r(t-1)-\delta}{2},                                  \tag{4.7}
$$
$$
 j=\frac{\delta}{4t}\big(r(t-1)^2-\delta t-1\big),\qquad
 k=-\frac{\delta}{4t}\big(r(t+1)^2+\delta t+1\big),            \tag{4.8}
$$
$$
 E=-\frac{\delta r}{2}+\frac{\delta r^2}{2t}
   -\frac{\delta}{4t}-\frac{\delta^2}{8}
   -\frac{\delta^2}{8t^2},\qquad C=j-E,\quad G=k-E.           \tag{4.9}
$$
这里 $r,t,\delta\ne0$，且无遗漏的被除零因子：$A=0$、$s=0$、$\delta=0$
均已逐支关闭，而 (4.5) 自身排除了 $r=0$。
把 (4.6) 代入后，(4.7)–(4.9) 实际都是 $\mathbb Q[r,t]$ 多项式。
配套原源还逐项确认全部四个原 mean 恒为零，因此不是放宽后的自由参数模型。

## 5. 一个特征零二变量成员门

令
$$
 \Phi=t^2+1,\qquad \Delta=4r^2-t^2-1,\qquad \delta=t\Delta/2.
$$
将 (4.6)–(4.9) 的真实 Gram 代入 (1.1)、(1.5)，按 (1.6) 定义八个局部值/jet，
再按 (1.7)、(1.8) 定义 $c_a,c_b,\mu$。
它们全部由这些原有理源式唯一重建。直接多项式除法给
$$
 \Phi^2\mid c_a,\qquad \Phi^2\mid c_b.                       \tag{5.1}
$$
定义
$$
 I=\left(c_a/\Phi^2,\ c_b/\Phi^2,\ \mu\right)
       \subset\mathbb Q[r,t].
$$
需要且只使用以下明确成员式：
$$
                    \Delta\Phi^2\in I.                    \tag{5.2}
$$
配套脚本从原源重建全部多项式，逐项检查原 mean 与 (5.1)。
令 $Q_a=c_a/\Phi^2,\ Q_b=c_b/\Phi^2$，改用同一理想的生成元
$$
 G_1=Q_a-Q_b,\qquad G_2=Q_a+Q_b+tG_1,\qquad G_3=\mu.
$$
它们的总次数为 $9,10,14$。各生成元只清除有理常数分母并取 primitive part，
不改变其有理理想。取所有
$$
 r^i t^jG_\ell,\qquad i+j+\deg G_\ell\le24
$$
作为来源列，在总次数至多 $24$ 的全部单项式行上组装精确整数矩阵。
它有 $325$ 行、$322$ 个来源列。模 $10007$ 消元仅确定一个 $294$ 阶非奇异子块；
随后用该**原整数子块**求有理乘子，把乘子写成整数列 $v$ 除以非零整数 $d$，
最后在**全部 $325$ 个原系数行**直接验证
$$
 M_{\rm selected}v=d\,\operatorname{coeff}(\Delta\Phi^2).
$$
这一全行整数乘积等式才是 (5.2) 的正证。模运算只选取可逆子块，
既没有提升模成员关系，也没有用上界假装原矩阵满秩。
该检查已实际通过，恢复和核验耗时见运行记录；不用再运行一般 Gröbner 消元。
不保存可重算的乘子、矩阵或消元输出表，只保存上述原源和完整构造算法。

若 $\Phi\ne0$，临界点的 $c_a=c_b=\mu=0$ 给 $I$ 中所有元素为零。
由 (5.2)，$\Delta\Phi^2=0$，与 $\delta=t\Delta/2\ne0$ 矛盾。
这里只在单独的 $\Phi\ne0$ 支路取消 $\Phi^2$。
下一节把 $\Phi=0$ 的全部例外保留下来显式处理。

## 6. $\Phi=0$ 的全部例外与原 Gram 秩矛盾

现在 $t^2=-1$。原源在此商环中的恒等式为
$$
 o=-n,\qquad \mu=3n^2,\qquad
 n=\frac{tr^2}{4}(2r^2-2tr-1).                              \tag{6.1}
$$
因 $r,t\ne0$，必要条件 $\mu=0$ 迫
$$
 2r^2-2tr-1=0,\qquad (2r-t)^2=1.
$$
因此只有
$$
 r=(t+1)/2\quad\hbox{或}\quad r=(t-1)/2.                     \tag{6.2}
$$
这些例外没有通过 $n$、$o$、$m$ 或任何 highest 值除掉。

在第一种情形，$\delta=-1,\ a=0,\ b=1$，且原活跃 Gram 与局部值为
$$
 K_B=\begin{pmatrix}
 0&0&1&(t-1)/2\\
 0&0&0&0\\
 1&0&0&0\\
 (t-1)/2&0&0&0
 \end{pmatrix},                                            \tag{6.3}
$$
$$
 p=(t+1)/4\ne0,\quad p_1=q=q_1=n=n_1=o=o_1=0.
$$
由原 (1.6)，$u\ne0,\ v=0,\ z=0$；原 $N$ 值又迫 $m=0$。
由 $m=a u+v+bz+w$，得 $w=0$。故
$U=(u,0,0,0)^T$ 已在 (6.3) 的像中。
该活跃 Gram 秩为二，扩充的零点列也在其像中，而且扩充对角为零。
更直接观察 (6.3) 与该 $U$：所有非零项仍只在一个星形行列中，
所以 $\operatorname{rank}\widehat K=2$，违反 (1.3)。

第二种情形是交换两个原双点：
$\delta=1,\ a=1,\ b=0$，
$$
 K_B=\begin{pmatrix}
 0&0&1&0\\
 0&0&-(t+1)/2&0\\
 1&-(t+1)/2&0&0\\
 0&0&0&0
 \end{pmatrix},                                            \tag{6.4}
$$
$$
 q=(1-t)/4\ne0,\quad p=p_1=q_1=n=n_1=o=o_1=0.
$$
原式给 $U=(0,0,z,0)^T$，全 Gram 同样只有秩二。
由此 $\Phi=0$ 的全部候选均被原五维 Gram 下界排除。

## 7. 结论、源与范围

由第 5 节实际通过的全行整数系数等式，
结合已支付的半权支路和第 2–6 节，外均值 essential-four 的
$$
 \operatorname{rank}H=4,\qquad D=(2+2)_{\rm unit}+1_{\rm zero}
$$
支路全部为空，任意 $a+b=1$ 均已包括。
证明未将长度四的有限呈示当成自由空间，未改动原 $K$，也未遗漏 $a=0$、$b=0$ 或局部极坐标零值。

可复算的完整源为[正规分支、原 QQ 乘子及全部 $\Phi=0$ 例外](../notes/2026-11-20-essential-four-unit-two-plus-two-general-isolated-zero-verify.py)，以及[独立边界和反向 mean 核验](../notes/2026-11-20-essential-four-unit-two-plus-two-boundaries-verify.py)。两份源均从原式重建，不载入计算表。

正规分支的实际完整执行为 run44730016169/job136267067883，冻结提交723f748d291139aeea1599a40224e02bab6b1430；全部325行整数乘积和最终例外检查通过，总计2.867秒，[运行身份](../notes/2026-11-20-exact-source-run44730016169-b2a9.json)保 source SHA、完整日志 SHA。独立边界执行为 run44731129539/job136270857160，冻结提交77d32165a6d85885e799c1b5c34712c60dd25a30，1.382秒全部通过，源码 SHA256 为 a2f39931923d3f1fc4f42f8372f0b0f3b566ce70bf205c22ae7bbc8cdae2cb24；[同批次运行身份](../notes/2026-11-20-exact-source-run44731129539-b2a9.json)区分各独立子进程结果。该 job 的另一份无关源码曾因未化简矩阵比较而失败，不改变已完整通过的本支检查。

只保存原算法、参数、运行身份和哈希；不保存可重算的乘子、矩阵或消元输出表。

本结论仍不处理孤立零点加单位 $3+1$、$2+1+1$、$1+1+1+1$，
也不关闭 unit rank-five、inner-mean 或本课题的普通 Hilbert ISP 主结论。
