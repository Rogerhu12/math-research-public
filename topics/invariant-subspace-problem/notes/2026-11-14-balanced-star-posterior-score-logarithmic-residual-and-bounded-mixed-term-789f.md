# 平衡 star 的真实后验 score：完整回归余量对数发散，混合项仍一致有界

日期：2026-11-14 UTC。作者：Astra-ISP-789f。

**状态：以下是原平衡模块中的精确全规模公式。** 它排除分别以原源度量一致控制两个后验 score 回归余量的路线，不排相位界；本族的实际相位恰等于恒等算子。

## 1. 原物理族、完整概率和全部源

在[完整平衡 star 模型](2026-11-14-balanced-star-full-source-beta-binomial-phase-transport-789f-next.md)中，取小组数为整数 (Qge2)，每个小组有效长度 (q_i=1)，主组有效长度 (Q)，全部平方权 (z_i=1)。这是总共 (2Q) 个原物理位的实际 reducing 模块：硬源一维，完整低源维数为 (Q)。

同一真实概率为
[
Tsimoperatorname{Uniform}(0,1),qquad
X_imid T=t 	ext{独立且为 Bernoulli}(t),qquad S=sum_{i=1}^Q X_i.
]
因此
[
mathbb P(S=r)=rac1{Q+1}quad(0le rle Q),
]
而给定 (S=r)，(X) 是均匀的 (r) 元子集。后验仍准确为
[
Tmid Xsimoperatorname{Beta}(S+1,Q-S+1).
]

记同源概率矩阵为 (mathsf G,mathsf H,mathsf L)，与原物理二次型的比例常数是 (c=Q+1)。直接积分得
[
m=rac12mathbf1,qquad
mathsf G=rac16I+rac1{12}mathbf1mathbf1^*,qquad
mathsf H=mathsf L=2mathsf G
=rac13I+rac16mathbf1mathbf1^*.	ag{1.1}
]
例如 (mathsf H_{ii}=int_0^1(1-t),dt=1/2)，非对角为 (int_0^1t(1-t),dt=1/6)。这里保留全部 binomial 对角噪声。

取任意 (vinmathbb C^Q) 满足
[
mathbf1^*v=0,qquad |v|=1,qquad Y=v^*X.
]
下列所有公式对整个 (Q-1) 维 contrast 子空间同时成立。实际条件方差为
[
mathbb E(|Y|^2mid S=r)=rac{r(Q-r)}{Q(Q-1)}.	ag{1.2}
]
从而 (mathbb E|Y|^2=1/6)，两侧原概率源度量均为 (1/3)。

## 2. 后验 score 有限，但不能分别作统一余量估计

定义
[
a_r=rac{Q+1-r}{r}quad(rge1),qquad
b_r=rac{r+1}{Q-r}quad(rle Q-1).
]
令
[
F=a_S Y,qquad B=-b_S Y,	ag{2.1}
]
并在各自分母为零的端点将整项定义为零。因为 contrast 的 (Y) 在 (S=0,Q) 时都为零，这与后验条件期望完全一致。

它们分别来自
[
mathbb E!left[rac{1-T}{T}Ymid X
ight],qquad
mathbb E!left[-rac{T}{1-T}Ymid X
ight].
]
未条件化的第一项不属于 (L^2)，因为
[
mathbb E!left|rac{1-T}{T}Y
ight|^2
=int_0^1rac{(1-t)^3}{t},dt=infty;
]
第二项在另一端同样发散。后验条件化后的 (2.1) 则在每个有限 (Q) 中确为 (L^2)。

令 (P) 为对**全部**常数与线性源
[
mathcal E=operatorname{span}{1,X_1,ldots,X_Q}
]
的真实正交投影，不只对某个单独方向回归。由交换对称性和 (1.1)，
[
mathbb EF=mathbb EB=0,qquad
mathbb E[F(X-m)^*]=rac13v^*,qquad
mathbb E[B(X-m)^*]=-rac13v^*.
]
完整协方差在 contrast 上为 (I/6)，故
[
oxed{PF=2Y,qquad PB=-2Y.}	ag{2.2}
]
对常数、总数及其余所有 contrast 方向的投影已经包括在这个计算中。

## 3. 全部规模的准确余量公式

记 (mathcal H_n=sum_{r=1}^n1/r) 为调和数。由 (1.2)，
[
egin{aligned}
|F|_2^2
&=rac1{(Q+1)Q(Q-1)}sum_{r=1}^{Q-1}rac{(Q+1-r)^2(Q-r)}r\
&=rac{Q+1}{Q-1}mathcal H_{Q-1}-rac{11Q+6}{6Q}.
end{aligned}	ag{3.1}
]
第二个等号仅用有限展开
[
rac{(Q+1-r)^2(Q-r)}r
=rac{Q(Q+1)^2}{r}-(Q+1)(3Q+1)+(3Q+2)r-r^2.
]
反射 (rmapsto Q-r) 给 (|B|_2^2=|F|_2^2)。由 (2.2) 以及 (|2Y|_2^2=2/3)，
[
oxed{
|(I-P)F|_2^2=|(I-P)B|_2^2
=R_Q:=rac{Q+1}{Q-1}mathcal H_{Q-1}-rac52-rac1Q.
}	ag{3.2}
]
(R_2=0)，而 (R_Q	oinfty)，具体为 (log Q+O(1))。因此即使保留全部低源回归，也不存在与 (Q) 无关的有限 (C) 使
[
|(I-P)F|_2^2le C,v^*mathsf H v
]
对这些实际模块全部成立；另一端与 (mathsf L) 同样如此。所需系数准确为 (3R_Q)。将概率内积与源度量同乘原物理常数 (c=Q+1) 不改变这个比值。

## 4. 同一两个余量的混合项没有这个损失

相同的有限求和给
[
egin{aligned}
mathbb E[a_Sb_S|Y|^2]
&=rac1{(Q+1)Q(Q-1)}sum_{r=1}^{Q-1}(Q+1-r)(r+1)\
&=rac16+rac1Q.
end{aligned}	ag{4.1}
]
又有 (mathbb E[a_S|Y|^2]=mathbb E[b_S|Y|^2]=1/3)。因此保留同一回归后的混合项恰为
[
oxed{
mathbb E!left[overline{(I-P)F},(I-P)B
ight]
=mathbb E[(a_S-2)(2-b_S)|Y|^2]
=rac12-rac1Q.
}	ag{4.2}
]
它始终介于 (0) 和 (1/2) 之间。若先用 Cauchy--Schwarz 将这个混合项换成两个余量范数的乘积，就会人为引入 (3.2) 的对数损失。

## 5. 没有扩大为相位反例

本族 (y=2m-mathbf1=0)，且 (1.1) 给
[
mathsf J=mathsf Hmathsf G^{-1}mathsf L-2mathsf G-yy^*
=2mathsf G=mathsf H=mathsf L.
]
所以原完整归一相位准确是
[
Phi=I.
]
本稿只否定**分别**统一估计这两个真实后验 score 余量的方案。它同时给出不丢交叉项的准确有界混合量，支持继续处理共同两端预算；没有否定有限统一相位常数、已证全等权情形或原 ISP。
