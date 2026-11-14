# R144：冻结平坦参考场的 lifting 与显式新初猜

**状态：已证明。** 本结论选择一个新的有限场表示来处理已定位的大负 $l$ 初猜。参考场在原 base 度量上准确；当半径设计参数改变时，只把它作为已知函数，完整保留新目标的 Gauss–Codazzi 缺陷。

## 1. 明确的对象

固定物理坐标 $(s,u)$ 与一个不随未知参数改变的计算角 $u=U(s,\xi)$。旧完整三场表示为
$$
f(s,\xi;p)=B(\xi)y(s)+L(s,\xi;p),
\qquad f=(n,m,l), \tag{1}
$$
其中 $y$ 是有限 Fourier correction 的径向 P1 系数，$p$ 含中央、尾与物理半径参数。$L$ 为已有完整 seed/tail lifting。

从 R139 固定一条 base $K=0$ coast 上的准确 native 场 $R(s,u)$。它的入口 Fourier 函数、base 参数与源身份全部固定，不用当前求解中的未知 $n$ 构造它。用同一固定计算角记
$$
\widetilde R(s,\xi)=R(s,U(s,\xi)).
$$
其真一阶导数是
$$
\widetilde R_s=R_s\big|_u+U_s R_u,
\qquad \widetilde R_\xi=U_\xi R_u. \tag{2}
$$
R139 保证参考 $n>0$，故其尚未直接列出的径向 $l$ 导数可由准确恒等式 $l=m^2/n$ 得到
$$
l_s=\frac{2m m_s n-m^2n_s}{n^2}. \tag{3}
$$
(3) 的分母是严格正的冻结参考函数，绝不是任意当前 raw 场的 $n$；原未知三场仍保持独立，允许未知 $n$ 为零。

## 2. 有准确端点迹的权重

设 coast 区间为 $[c,c+L_c]$，选 $0<\varepsilon<1/2$、$r=\varepsilon L_c$。令
$$
S_5(q)=10q^3-15q^4+6q^5
$$
在 $q\le0$ 延为0、在 $q\ge1$ 延为1，并取
$$
w(s)=S_5((s-c)/r)S_5((c+L_c-s)/r). \tag{4}
$$
则 $0\le w\le1$；在 coast 外为0，在 $[c+r,c+L_c-r]$ 为1，并且两端 $w=w'=w''=0$。因此无需把 $R$ 延拓到 coast 外；乘积 $w\widetilde R$ 在两端按零延拓即可保持所需的连续值和角 jet，且权重本身为 $C^2$。当前具体选择是 $\varepsilon=.12$。

定义新 lifting
$$
\widehat L=(1-w)L+w\widetilde R. \tag{5}
$$
中央柱和真实切口都在权重支撑外，故原准确 seed 边界、tail 全函数切口及全部已有参数约束保持原定义。没有替换目标 $a_\delta(s)$、物理域或 gap。

## 3. 完整空间导数与参数列

直接对 (5) 求导，得到
$$
\widehat L_s=(1-w)L_s+w\widetilde R_s+w'(\widetilde R-L),\qquad
\widehat L_\xi=(1-w)L_\xi+w\widetilde R_\xi. \tag{6}
$$
因为 $w,\widetilde R,U$ 都固定，对每个未知参数有
$$
\widehat L_p=(1-w)L_p,\qquad
\widehat L_{s,p}=(1-w)L_{s,p}-w'L_p,\qquad
\widehat L_{\xi,p}=(1-w)L_{\xi,p}. \tag{7}
$$
(6)–(7) 是值、物理计算径向一 jet、角一 jet 与参数列的完整公式。漏掉 $-w'L_p$ 将产生错误 Jacobian。

对于半径设计参数，还必须对当前目标的 $1/a_\delta$、$a'_\delta/a_\delta$、$K_\delta$ 求导。不能把旧的完整 forcing 参数列一律乘 $(1-w)$：新参考项也乘着当前目标连接系数。具体实现先用 (5)–(7) 构造新 lifting 的真实各 jet，再用原三场方程与当前目标系数重新形成 forcing 和它的全部 profile 列。独立 $l$ 及中央节点的线性消元规则保持不变。

## 4. 这是参考函数，不是借来的新度量解

R139 的 $R$ 准确满足 base coast 的 $K=0$ 方程。当 $\delta\ne0$ 时，当前目标 $a_\delta$ 通常不再具有相同连接或零 Gauss 曲率。

例如在 $w=1$、correction 为零的整段上，新完整场就是固定 $R$。它在当前度量下的 Gauss 残差准确是
$$
G_\delta=R_nR_l-R_m^2-K_\delta=-K_\delta. \tag{8}
$$
两条 Codazzi 同样要用当前 $a_\delta$ 重新计算。参考值在新正交框架中只是明确指定的候选分量函数，不自动等于某个已知位置图在新度量下的实际第二基本形式。base 的位置、metric、reach 或正常球界均不因此转移。

这说明在当前 target $K$ 较小时，(8) 可以成为有针对性的初猜；它绝不把改过的目标宣布为准确等距，也不省略任何新的缺陷。

## 5. 必须真正改变坏初猜

若只是保持旧场的低模式并重新分配 lifting/correction，可能会继续保留已定位的大负 $l$ 分支。这里明确选择新的节点初猜
$$
\widehat y_j=(1-w(s_j))y_j,
$$
而保持所有 $p$ 不变。由 (1) 与 (5)，在每个原节点准确有
$$
B\widehat y_j+\widehat L(s_j)
  =(1-w(s_j))f(s_j)+w(s_j)\widetilde R(s_j). \tag{9}
$$
所以参考平台节点的旧 correction 被清零，中央及切口节点不变。若旧节点已经满足准确柱/切口消元，新的边界投影也不会再改变这些节点；否则应记录实际投影变化，不能暗中忽略。

节点之间仍以 $\widehat y_j$ 作 **P1 插值**，而不是定义 $\widehat y(s)=(1-w(s))y(s)$。两者相差
$$
P_1\bigl((1-w_j)y_j\bigr)(s)-(1-w(s))P_1(y_j)(s), \tag{10}
$$
一般不为零。因此 (9) 是节点恒等式；所有格内 Gauss/Codazzi 必须消费实际新 P1 场与 (5)，不能直接从节点的凸组合推断连续残差或曲率界。若一个完整单元位于 $w=1$ 平台且其两端新 correction 为零，则该单元才确实处处等于参考函数。

## 6. 实现与结果范围

`CoastReferenceRawBumpDAE` 使用 `FrozenCoastReference` 的明确固定输入与缓存；缓存必须同时绑定物理 $s$ 和实际材料角列，不能仅凭同一个 $s$ 借用其他角图的数据。每次预计算仍来自 R139 的函数定义，有限求逆误差及实际源身份另行记录。

这一操作不改当前参数与目标度量，但明确改变了有限场表示和初猜。它不是旧场的无误差复制，不是非线性求解成功，也不是同 $g$ 加密完成。后续仍须实际求解完整方程，支付实际位置/两 jet、连续误差、闭合、全时嵌入与强比例。

## 7. D2 对称与行压缩的适用性

若冻结入口 $n_c$ 是偶函数、$m_c$ 是奇函数且二者均 $\pi$ 周期，则 $k=m_c/n_c$ 为奇函数，$k_t,Q,w,D$ 为偶函数。R139 的角映射因此满足 $U(\sigma,-t)=-U(\sigma,t)$ 和 $U(\sigma,t+\pi)=U(\sigma,t)+\pi$。其严格正导数保证唯一逆映射也有这两个恒等式，故物理 $n,l$ 为偶函数、$m$ 为奇函数。旧角图具有相同对称，径向权重不改角对称；(5) 及所有参数列仍在 R142 的 D2 子空间中。因此 R142 的行压缩适用于这一新表示的完整有限离散。实际缓存材料反解的浮点误差仍由各次检查报告保留，不从解析对称推断浮点逐位零误差。
