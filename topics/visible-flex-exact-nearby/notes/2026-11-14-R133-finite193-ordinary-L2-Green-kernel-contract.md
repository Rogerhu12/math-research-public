# R133：已成完整 signed Green 端口的真正径向 L2 核消费合同

2026-11-14，visible-exact / tail_connector。

本合同只把已经成功的完整 193 状态 positive Green 端口重新用于
普通体源的 $L^2_r$ 输入。它不重算 projector、frame、Riccati、
原 body 源或 cap 目标。所有原 sec/tan 接口、最后腰端跳、
独立 mean、真实 cap/腰边界和已付严格 margin 原样保留。

结论是同一个有限 193 压缩问题的
$G_L:L^2_r(\text{ordinary pair})\to C^0_r$ 与
$L^2_r\to L^2_r$ 上界。未知 high 输入和实际 cap 的完整
cross-block/affine 输入仍是原端口，不能据此宣布全 PDE 逆成立。

## K.1. 原比较系统与完整输入归一

每个原连续事件使用同一常数上包络
$$
 p'\le\mu p+cq+f,\qquad
 -q'\le\nu q+ep+g,\qquad c,e\ge0,
$$
$$
 \mathsf A=\begin{pmatrix}\mu&c\\-e&-\nu\end{pmatrix}.
 \tag{K.1}
$$
$\mu,\nu$ 保留符号；只在原局部 no-pole 门中允许使用矩阵范数。
$p,q$ 是原正交子空间范数，mean 也是完整 193 状态之一。

用 $\omega(r)$ 表示原物理到能量状态的权，避免与 Riccati 斜率
$\varrho$ 混名。若 $S_\omega$ 为原变换，选同格已知
$$
 w_i\ge\sup_i\|S_\omega\|,\qquad
 k_i\ge\sup_i\|S_\omega^{-1}\|.
$$
原对角变换可用 $w_i=\max(1,\omega_{\max})$、
$k_i=\max(1,\omega_{\min}^{-1})$，并保留原普通 pair/193
正交归一。设原 complementary 正交投影为 $P(r),Q(r)$，
定义两个标量输入
$$
 u_1={\|P S_\omega F\|\over w_i},\qquad
 u_2={\|Q S_\omega F\|\over w_i}.
$$
准确有
$$
 |u_1|^2+|u_2|^2
 ={\|S_\omega F\|^2\over w_i^2}\le\|F\|_{\rm ordinary}^2.
 \tag{K.2}
$$
因此所有互斥连续区间的 $\bigoplus L^2(\mathbb R^2)$ 输入范数
不超过原完整 ordinary 源范数。这里没有把两个投影都换成同一个
源范数后误当作正交，也没有删除独立 even mean。

## K.2. 只读取原端口；不假设未保存的 T(h) 存在

原连续端口已给非负上界
$$
 z_L\le a z_R+Q_i u_i,\qquad
 p_R\le b p_L+k z_R+P_i u_i,
 \tag{K.3}
$$
以及原右锥 $\varrho_R=r\ge0$、长度 $h$、signed
$\mu,\nu,c,e$ 和完整 suffix no-pole 证书。
原 compact event 可能没有保存 transfer matrix；
本消费者不要求该字段，也不重算原端口。

为证明新的局部输入核，暂记
$T(\tau)=\exp(\tau\mathsf A)$、
$D=\operatorname{diag}(1,-1)$、$v_q=(r,-1)$。
若写准确局部端口，则
$d=T_{22}(h)-rT_{12}(h)>0$、
$a_{\rm ex}=1/d$、$k_{\rm ex}=T_{12}(h)/d$。
原完整 positive Green/no-pole 证明保证
$$
 v_qT(\tau)D\ge0 \quad(0\le\tau\le h)
 \tag{K.4}
$$
逐分量成立。采用原已经合法向上取整的 $a,b,k$，可使用新的
完整核上界
$$
 \widehat Q_i(s)=w_i a\,v_qT(h-s)D,
$$
$$
 \widehat P_i(s)=w_i( (1+rk),-k)\,T(h-s)D.
 \tag{K.5}
$$
第一式从 $a\ge a_{\rm ex}$ 得到。第二式是
$w_i(e_1+k v_q)T(h-s)D$；将 $k_{\rm ex}$ 增至 $k$
增加的是原非负核 (K.4)，故整条核仍非负且逐项上界真实核。
这不要求 $T$ 本身逐项非负。

实际读入的 $r$ 必须仍由原完整 suffix 门覆盖；
不能在消费者中换一个未经验证的更大锥。
原所有记录球、率和长度用定向区间读取，保留其准确数学对象。

## K.3. 一次新的小型 Lyapunov 核积分

只计算
$$
 G(h)=\int_0^hT(\tau)T(\tau)^T\,d\tau .
 \tag{K.6}
$$
它的三个独立分量从零出发满足
$$
 \begin{aligned}
 g_{11}'&=2\mu g_{11}+2c g_{12}+1,\\
 g_{12}'&=-e g_{11}+(\mu-\nu)g_{12}+c g_{22},\\
 g_{22}'&=-2e g_{12}-2\nu g_{22}+1 .
 \end{aligned}                                       \tag{K.7}
$$
把常数 1 加作第四状态即可用一个新的 $4\times4$ 定向指数积分。
这是新核平方积分，不是再次运行原 $193\times193$ 传播或目标。
$D D^T=I$，所以
$$
 \|\widehat Q_i\|_{L^2\to\mathbb R}^2
 \le w_i^2 a^2\,v_qG(h)v_q^T .
 \tag{K.8}
$$
所有二次型必须先用完整有向 $G$ 球与带符号的行向量求值，再取
合法非负上端。不能先逐元素把 $G$ 换成 upper 后乘负系数。
$g_{12}$ 的符号也不得人为改为正。

同一核向量的和应在积分前合并；不能对 $Q,P$ 分别取 norm
后把它们的相关性删掉。

## K.4. O(N) 的完整左右源支集分解

只研究 ordinary 体源通道时，两端外部 affine 负荷为零，
原边界条件及其完整反馈仍保留。设原
$\mathrm{margin}=1-D_0\varrho_0>0$。
后扫定义 $Z_i^2$ 为 $z_i$ 对全部右侧源的行核平方范数：
$$
 Z_R^2=0\ \hbox{在最外端},\qquad
 Z_L^2\le a^2Z_R^2+\|\widehat Q_i\|^2.
 \tag{K.9}
$$
两项对应互不相交的径向源支集，所以是平方和。

前扫保持形式
$$
 p_i\le v_i z_i+w_i^{\rm past},
 \qquad
 v_0={D_0\over\mathrm{margin}},\qquad
 \|w_0^{\rm past}\|=0 .
$$
$w_i^{\rm past}$ 只依赖该节点左侧的源；
它不是 K.1 的局部输入权 $w_i$。记其行核平方范数为 $W_i^2$。
有
$$
 v_R=bv_La+k,\qquad
 W_R^2\le b^2W_L^2+
          \|bv_L\widehat Q_i+\widehat P_i\|^2 .
 \tag{K.10}
$$
局部核的准确组合是
$$
 bv_L\widehat Q_i+\widehat P_i
 =w_i((1+rv_R),-v_R)\,T(h-s)D.
$$
故
$$
 \|bv_L\widehat Q_i+\widehat P_i\|^2
 \le w_i^2((1+rv_R),-v_R)
           G(h)((1+rv_R),-v_R)^T .                   \tag{K.11}
$$
$v_R$ 若进一步向上舍入，增加的仍是
$w_i(v_R^{\rm new}-v_R)v_qT D\ge0$，所以合法。

每个原 sec/tan projector 接口照原已付端口使用 $a,b,k$，
局部体源核为零；因此仍用
$$
 Z_L^2\le a^2Z_R^2,\qquad
 v_R=bv_La+k,\qquad W_R^2\le b^2W_L^2 .
 \tag{K.12}
$$
最后腰端的原零长接口也保留。不能把 $\sin\theta$ 当作
$\tan\theta$，或把两个对角 sec 因子设为1。

## K.5. 节点两分量的完整 Gram 与连续格费用

在节点 $i$，过去源与未来源正交。因
$q_i\le\varrho_i p_i+z_i$，完整两分量 Gram 上界为
$$
 \mathcal G_i=
 W_i^2\binom1{\varrho_i}(1,\varrho_i)
 +Z_i^2\binom{v_i}{1+\varrho_i v_i}
                 (v_i,1+\varrho_i v_i).
 \tag{K.13}
$$
同一 ordinary 单位输入的节点状态范数不超过
$k_i\sqrt{\lambda_{\max}(\mathcal G_i)}$。
取 trace 是合法的较粗替代。
真实 jump 两侧都要消费其各自的原物理变换。

为了覆盖整个连续格，首版可以使用一次局部 Minkowski，
不需要新的高维 Gram 传播。令原完整 suffix 证明给
$\bar\varrho\ge\sup_{[0,h]}\varrho(s)$，取
$$
 \lambda_z=\nu+c\bar\varrho,\qquad
 \lambda_p=\mu+c\bar\varrho,\qquad
 I(\lambda,h)=\begin{cases}(e^{\lambda h}-1)/\lambda,&\lambda\ne0,\\h,&\lambda=0.\end{cases}
$$
$\mu,\nu$ 的符号仍保留。
对于整格任意位置，右侧外源与本格源正交，故可用
$$
 Z_{\rm whole}^2
 \le\max(1,e^{2\lambda_z h})Z_R^2+
        w_i^2(1+\bar\varrho^2)I(2\lambda_z,h).
 \tag{K.14}
$$
左节点的完整 $p$ 行核范数为
$P_L=(W_L^2+v_L^2Z_L^2)^{1/2}$。
原 Riccati 正 Green 标量式给
$$
 P_{\rm whole}\le
 \max(1,e^{\lambda_p h})P_L+
 c I(\lambda_p,h) Z_{\rm whole}
 +w_i\sqrt{I(2\lambda_p,h)},
$$
$$
 Q_{\rm whole}\le\bar\varrho P_{\rm whole}+Z_{\rm whole}.
 \tag{K.15}
$$
最后两式只在这一格作一次 Minkowski。
$P_L$ 已含本格源，不能再声称它与右端或局部 forcing 正交。
(K.14) 的平方和则确有 disjoint support 依据。
这里没有把常数源 sup 消费器乘 $\sqrt h$ 冒充任意 $L^2$ 源逆。

令
$C_i=k_i(P_{\rm whole}^2+Q_{\rm whole}^2)^{1/2}$。
则完整区间上
$$
 \|G_L\|_{L^2_r\to C^0_r}
 \le\max\{\sup_i C_i,\ \hbox{全部接口节点界}\},
$$
$$
 \|G_L\|_{L^2_r\to L^2_r}
 \le\left(\sum_i h_i C_i^2\right)^{1/2}.
 \tag{K.16}
$$
积分使用真实 $dr$，若原 port 坐标另有变换，输入权、输出权和
$h_i$ 必须按原已有 Jacobian 同时转换，不能只改一侧长度。
原 6391 源分片、5970 frame 接口和所有细分事件按照准确有序
cover 逐项处理；数量以实际成功原 native 为准。

## K.6. 必须保存的证据与范围

新 native 需绑定原完整 Green/过程、全部 compact events、
原 waist margin、左右边界和输入/输出物理转换的 SHA。
逐连续格保存 signed 率、$r$、$a,b,k$、输入 $w_i$、输出 $k_i$、
新的 $G$ 球及两个完整二次型上界；保存后扫 $Z^2$ 和前扫
$v,W^2$ 的完整 cover。接口也有自己的记录，不能从连续格总数
推断接口已消费。

任一 no-pole、margin、正转换下界、native identity 或有序 cover
门失败即不授全区结论。新数值只在公开仓库 Actions 执行；
不改任何旧已成 native，也不重跑原数学源。

该 $G_L$ 是同一个完整有限 193 operator 的 ordinary 源列。
原 cap/head/high 的双向 cross-block 仍是完整系统的一部分：
对给定 high/端口输入的响应列保持原消费合同，不因本篇新增
ordinary 列的更紧范数而删除。真实未知 high Schur 与完整
$\nu$ 行仍需另外支付。
