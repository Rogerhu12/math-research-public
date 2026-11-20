# 全闭同一度量中的物理全局修正

2026-11-20，Astra-larger-resume-24b2ab87 / geometry_path。
本稿给出可直接加入现有全闭模型的有限维搜索空间；它不宣称该空间含有精确解。
数值拟合一旦执行，实际结果与源 SHA 另记。

## 1. 联动帽高度，消除人为局部梯度

原模型是

$$F=q+\chi(s)\{[R+S-s]e_r(\Theta(\phi))+H e_z\}.$$

固定原 $g,a,S,R,\Theta$ 以及全部 core 系数。单独改 $H$ 时，实际径向导数出现
$\chi'(s)\delta H e_z$；它集中在原宽 $w=.05$ 的末段。这是坐标方向的局部效应，
不是高度自由度自身必须产生的大梯度。

令

$$B(s)=10(s/S)^3-15(s/S)^4+6(s/S)^5.$$

取联动方向

$$\delta H=1,\qquad \delta q_Z=B-\chi,\qquad \delta q_R=\delta q_T=0.$$

则在该表达式按字面成立的模型中，准确有

$$\delta F=B e_z,\quad\delta F_s=B'e_z,\quad\delta F_{ss}=B''e_z,$$

且 $B(0)=B'(0)=B''(0)=0$，$B(S)=1$、$B'(S)=B''(S)=0$。
因此 core 的三 jet 保持，末圆盘只作共同竖直平移，末端剩余 $q$ 的三 jet 仍全零。
$\max|B'|=15/(8S)$，不含 $1/w$ 的大因子。

实际脚本存储 $B-\chi$ 的节点三 jet，再由原 shared-quintic 算子求值。
若 $\chi$ 的分界点为同一准确网格节点，两个分段都是五次多项式，Hermite 唯一性给上述
恒等式在全域准确成立。无论浮点载体的分界是否逐字重合，脚本消费的都是
原插值的真实导数加解析 $\chi'$，没有用理想 $B'$ 偷换；末两端条件仍逐字为零。

## 2. 覆盖完整径向区间的低频物理方向

在原网格选定依次邻近 $.60,1.05,1.35,1.75,2.15$ 的五个节点，连同两端组成
$0=t_0<t_1<\dots<t_5<t_6=S$。对每个内部 $t_k$，定义 $b_k$：
在 $[t_{k-1},t_k]$ 为从 0 到 1 的五次 smoothstep，在
$[t_k,t_{k+1}]$ 为从 1 到 0 的五次 smoothstep，其余为零。
它在两个支撑端及峰值点的一、二导数均为零，因而是准确的 $C^2$ 分片五次函数。
在原细网格存入它的三 jet 后，原 shared-quintic 精确表示同一函数。

令 $\nu=2m$。在原旋转 $\phi$ 正交标架中选取角向向量

$$h_{R,m}=(\cos\nu\phi,0,0),\quad
h_{T,m}=(0,\sin\nu\phi,0),\quad
h_{Z,m}=(0,0,\cos\nu\phi).$$

使用 $R/Z$ 零模与 $m=1,2,3$ 的三组方向，共 11 个角向通道。
每个 $b_k h$ 给一个物理修正 $\delta F=b_k h$。
全部 55 个方向在 core 和 cuff 的三 jet 都为零。
第一个径向方向支撑从 $s=0$ 开始，所以这个搜索空间并未永久冻结原有 prefix。

另令 $c(s)=(s/S)^2(1-s/S)^3$。有
$c(0)=c'(0)=0$、$c''(0)=2/S^2$，末端三 jet 全为零。
只将它用于上述 7 个水平 $R/T$ 通道；这恰改变原模型允许自由变化的
$A_{0,XY}$，不改变 core 位置、$U_0=e_z$ 或 $A_{0,Z}=0$。
连同联动高度方向，搜索维数为 $55+7+1=63$。
原 1,332,245 个自由度没有被宣称等价消去；63 维拟合只生成供完整求解器继续使用的初猜。

## 3. 保持完整 Gram 目标的小矩阵

记原同一真实候选在各完整 stage/角点的导数为 $V=F_s,d=F_\phi$。
本搜索不变动 core，故 $\rho,\Theta$ 与所有分母 $a\rho$ 全部固定。
对一个方向 $\delta F=b(s)h(\phi)$，

$$\delta V=b'h,\qquad \delta d=b D_\phi h,$$

其中 $D_\phi$ 包括旋转标架联络，明确为

$$D_\phi h_{R,m}=(-\nu\sin\nu\phi,\cos\nu\phi,0),$$
$$D_\phi h_{T,m}=(-\sin\nu\phi,\nu\cos\nu\phi,0),$$
$$D_\phi h_{Z,m}=(0,0,-\nu\sin\nu\phi).$$

原三个归一 Gram 项 $(r_0,r_1,r_2)$ 的导数准确为

$$\delta r_0=2V\cdot\delta V,\quad
\delta r_1=(d\cdot\delta V+V\cdot\delta d)/(a\rho),\quad
\delta r_2=2d\cdot\delta d/(a\rho)^2.$$

所以可在缓存的同一 $V,d$ 上逐 stage 累积 $J^TWJ$ 和 $J^TWr$，
$W$ 保持原 Frobenius 权 $(1,2,1)$。没有为每个方向重新求 base 场，
没有截去原任何径向、角向或 Gram 方程，也没有改变 least-squares 目标。
非线性候选只改变 $V,d$ 的线性组合，残差仍按原完整二次表达式重新求值。

计算同时消费 R653 的四分之一角轨道恒等式：端点 multiplicity 为 2、内部为 4；
Jacobian 和 residual 都乘同一个平方根权，因此与原 N2048 全圆目标相同。
这些是对称性归并，不是少检查三分之二的方程。

完整方向的首末阶信息仍取原插值场；最终候选再直接调用原目标的 batch 实现读出。
所有 determinant、Gram 峰值及 merit 都只标为浮点有限点值，不冒作连续嵌入/reach 认证。

## 4. 执行入口

`fullclosed_physical_subspace.py` 接收原 bundle、原 dense source，以及 R653 batch source；
以 `--quarter --angles 2048 --low-modes 3 --steps 6` 执行一个固定六步拟合。
每步允许固定 8 个二进回溯步，当前点完整目标决定是否接受；域诊断要求所有实际点值
Gram determinant 为正。所有接受与拒绝均写入同一新报告。
输出完整候选仍在 scratch，最终可公开保存的内容为脚本、参数、输入与输出 SHA 和紧凑记录。

这一步不支付全域误差、同 $g$ 精化、全闭 reach、握持量或含反射非全等；若改善了初猜，
后续仍在原完整空间继续求解。
