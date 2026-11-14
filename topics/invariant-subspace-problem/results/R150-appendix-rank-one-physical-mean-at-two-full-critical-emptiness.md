# R150 补篇：物理均值参数二的全部临界点与零三阶张量

日期：2026-11-14。作者：Astra-ISP-1cf8c51d。

## 1. 定理及完整范围

在原六模模型中令
$$
v(s)=(1,s,s^2,s^3,s^4,s^5)^{\mathsf T},\qquad y=v(2).
$$
设原最高方程和其余全部十七条临界方程成立，且
$$
H=M+\frac12yy^{\mathsf T},\qquad M_{ij}=m_{i+j}.
$$
那么存在 $c,d\in\mathbb C$，使
$$
M=c\,v(2)v(2)^{\mathsf T}
+d\bigl(v(2)v'(2)^{\mathsf T}+v'(2)v(2)^{\mathsf T}\bigr).
\tag{1.1}
$$
这些 $M$ 全部给出原临界点，最高方程唯一恢复相应 $V$，并且所有点均有 $T_3=0$。

因此 $s=2$ 的非零三阶完整临界分支为空。结论不附加 $A_yM=0$、$MKM=0$、本质变量数或均值位置条件。对任意非零振幅 $y=av(2)$，把 (1.1) 右侧乘 $a^2$ 即为全部 $M$。这只是指定有限标量分支的完成，不宣告普通 Hilbert 空间不变子空间问题完成。

## 2. 原方程的可逆矩坐标平移

使用
[原秩一均值完整中心化归约](R150-appendix-rank-one-physical-mean-centered-complete-critical-reduction.md)：
$$
\mathcal L_y(M)=J_3^{-1}[p_yJ_2(M)],\quad
V=\frac32\mathcal L_y(M)+\frac12y^3,\quad
T_3=6(\mathcal L_y(M)-yM).
$$
剩余完整方程为
$$
N(Kv(t),Kv(t))\equiv0,\qquad
N=4MKM+6(\mathcal L_y(M))_{Ky},
$$
及
$$
\Gamma=2\tau_2(M)y+8MKM(Ky)
-12\mathcal L_y(M):(KMK)=0.
$$
取前者关于 $t$ 的十一项系数及后者六个原坐标，合计十七式。全过程保留原 $K$ 和原物理曲线，没有把第一条曲线恒等式加强为全矩阵恒等式。

引入三角整数坐标变换
$$
m_k=\sum_{j=0}^{k}\binom{k}{j}2^{k-j}n_j,
\qquad
n_j=\sum_{k=0}^{j}\binom{j}{k}(-2)^{j-k}m_k.
\tag{2.1}
$$
其对角线为一，所以在特征零中可逆。令
$$
c=n_0,\quad d=n_1,\quad z=(n_2,\ldots,n_{10}).
$$
切向平面 $z=0$ 正好对应 (1.1)，即
$$
m_k=2^k c+k2^{k-1}d.
$$
$k=0$ 时第二项按零计。

整系数原式由已发布的
[原系统生成器](../notes/2026-11-14-rank-one-centered-integer-system-generator.js)
从原 $K,\operatorname{adj}(J_3),\det(J_3)$ 和参数 $s=2$ 重建，再经
[可逆平移生成器](../notes/2026-11-14-rank-one-centered-translation.js)
逐项代入 (2.1)。每行仍记录非零整数比例，行的最大公因数和符号归一化都同步乘入该比例。因此所得 $f_1,\ldots,f_{17}$ 与原方程具有完全相同的复零点。

规范变换后系统 JSON 的 SHA256 为：
~~~text
8462b48b8b9270df73f297704a5e63444a44c972b5e675cf25884c189e70b03e
~~~
不需要传输新的大系数表：原数据、完整生成器、参数和哈希已明确指定全部系数。

十七个 $f_i$ 都无常数项、总次数至多二，并且 $f_i(c,d,0)=0$。后者也可直接从原自接触条件看出：$K$ 在 $\operatorname{span}(v(2),v'(2))$ 上恒为零。脚本逐项检查所有纯切向线性、二次系数确为零。

## 3. 170 行小投影的两个完整整数核

令
$$
\mathcal R=\operatorname{span}_{\mathbb Q}
\{n^\alpha f_i:|\alpha|\le3,\ 1\le i\le17\}.
$$
这是总次数一至五的 $6188\times4367$ 指定整数系数矩阵的行空间，其中
$$
6188=17\binom{14}{3},\qquad4367=\binom{16}{5}-1.
$$
按横向变量因子数分列，纯 $c,d$ 项为 20 列，恰一个横向因子为 135 列，至少两个横向因子为 4212 列。$\mathcal R$ 的纯切向项全为零。

保留恰一个横向因子的投影记为 $\pi$。只有十个纯切向乘子 $c^ad^b$、$a+b\le3$ 能有非零投影，因此 $\pi\mathcal R$ 是一个 $170\times135$ 整数矩阵 $P_2$ 的行空间。列按
$$
c^ad^bn_j,\quad
a+b=0,\ldots,4,\quad a=0,\ldots,a+b,\quad j=2,\ldots,10
$$
依次排列；行按原十七式、乘子总次数、$a$ 排列。

[本分支小证书](../notes/2026-11-14-rank-one-physical-mean-two-rank-certificate-receipt.json)
直接保存两个完整的 135 坐标整数向量 $q_1,q_2$，满足
$$
P_2q_1=P_2q_2=0.
$$
原矩阵逐行精确代入的 340 个整数余项均为零。自由列为零起算的 $8,26$，即 $n_{10},c n_{10}$；各向量在这两个自由列中只有自己的一个坐标非零，故独立。

第一个核仅在九个零切向次数列有支撑，值为
$$
(450893776115,\ -1197502707740,\ 2158222209920,\
-3705158780600,\ 6258015491440,\ -10501608289680,\
17591420832800,\ -29468902513952,\ 49236573805600).
$$
两个完整核的规范 JSON 的 SHA256 为
~~~text
2c826b68529d87222a4c2367d152fb715ec50d353a129fe061f55a32c20a23cd
~~~
故
$$
\operatorname{rank}_{\mathbb Q}P_2\le133,\qquad
\dim_{\mathbb Q}\mathcal R\le4212+133=4345.
\tag{3.1}
$$

## 4. 模十一的匹配下界与理想包含

同一原整数倍式矩阵在 $\mathbb F_{11}$ 上精确消元，得到秩 4345。总次数一至五的枢轴数量依次是
$$
7,\ 63,\ 282,\ 996,\ 2997.
$$
4345 阶模十一非零子式在 $\mathbb Q$ 上也非零，所以
$$
\dim_{\mathbb Q}\mathcal R\ge4345.
\tag{4.1}
$$
本篇选择模十一完成整数秩下界；模七在该特殊点的进一步退化不参与证明。没有依据有限域点集推断复数点集。

由 (3.1)、(4.1)，
$$
\dim\mathcal R=4345
=\dim(\mathcal R\cap\ker\pi)+\dim(\pi\mathcal R).
$$
右侧两项分别至多 4212 和 133，故第一项达到 4212，即
$$
\ker\pi\subset\mathcal R.
$$
因此总次数至多五、至少包含两个横向因子的全部多项式都属于原十七式的理想。特别地
$$
n_j^2\in\mathcal R\subset(f_1,\ldots,f_{17})
\quad(2\le j\le10).
$$
任一复数解必有 $n_2=\cdots=n_{10}=0$，证明 (1.1)。

所附模十一程序用四个位平面记录域元素，逐位进位后按常数十一作条件减法。每个非零枢轴缓存其十个标量倍数；所有加法和归一化都在有限域内精确进行。程序明示列举 121 种域加法恒等式，每个枢轴还检查十个缓存倍数的首系数，整段没有浮点容差。

## 5. 反向与三阶张量

在 (1.1) 上，$yM$ 是三阶 Hankel 张量，并满足
$$
J_3(yM)=p_yJ_2(M).
$$
$J_3$ 可逆，故 $\mathcal L_y(M)=yM$，从而 $T_3=0$。

原物理核为 $k(s,t)=-(t-s)^2q(s,t)$，且
$$
q(s,s)=-s^2(s-2)(s+6).
$$
因此
$$
v(s)^{\mathsf T}Kv(s)=v(s)^{\mathsf T}Kv'(s)=0,\qquad
v'(s)^{\mathsf T}Kv'(s)=2q(s,s).
$$
在 $s=2$，该切向平面为 $K$ 各向同性，故 $MKM=0$、$M(Ky)=0$。于是 $N=0$，并由
$$
(yM):(KMK)=\frac13\{\tau_2(M)y+2MKM(Ky)\}=0
$$
得到 $\Gamma=0$。反向完成。非零振幅情形按原权重 $M\mapsto a^2M,\ V\mapsto a^3V$ 归一化；$N,\Gamma,T_3$ 的权重分别为四、五、三。

## 6. 完整重建入口

从仓库根目录运行：
~~~sh
node topics/invariant-subspace-problem/notes/2026-11-14-rank-one-translated-contact-rank-certificate.js 2
~~~
[入口脚本](../notes/2026-11-14-rank-one-translated-contact-rank-certificate.js)
重建原系数及三角坐标变换，核对系统和两核哈希，执行 340 项原整数核等式，再通过
[模十一大矩阵程序](../notes/2026-11-14-rank-one-exceptional-mean-macaulay-f11.js)
获得匹配下界。投影程序保留原零与无穷分支的行为，并支持本篇两个核。证书是证明中的有限精确资料，不另设独立审核门槛。

本篇关闭 $s=2$ 的完整分支；$s=-6$ 和其他物理参数仍按各自原方程继续，不作固定点间的无证外推。
