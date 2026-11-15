# R150：同选normal4高块的特征零秩1355、完整130维核与剩余交空间

日期：2026-11-15 UTC。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

本稿完成同一原 $I,J$、第二自然左连接中normal4校正在旧高零行上的完整特征零核。实际秩为1355，核维数为130；全部225680个原高行产品严格为零。130是校正自由量，不是新增的左延拓头。原完整第二连接仍只有 $9\le\beta_2\le11$ 的已付区间。

## 1. 固定原方程与高块

沿[同一第二连接22头](R150-appendix-selected-natural-second-left-twenty-two-heads-and-rank-interval.md)，保原4354个来源 $J$、完整旧36个右端和已经实际求出的旧单位解。最后一个系数的旧校正写成
$$
M'_0x+R\theta=0,\qquad
M'_0\in\mathbb Q^{4354\times1546},\quad R\in\mathbb Q^{4354\times36},
$$
其中 $\theta=(t,c)$，$t\in\mathbb Q^3$，$c\in\mathbb Q^{33}$；保原两个不同的 $E$ 嵌入及一阶、常核自由度。

在旧1736个高行上，$M'_0$ 和 $R$ 全部严格为零。加入同一选定输出 $I$ 中所有1485个normal4坐标，得到
$$
M_4=(A_0)_{I,J}^{\mathsf T}E_4,\qquad
H_4=(M_4)_{\rm high}\in\mathbb Z^{1736\times1485}.
\tag{1.1}
$$
这里的整数形式沿原已付行归一化；完整 $M_4$ 的全部4354行由原常数系数构造，没有另选来源或删掉高约束。

[首次完整剖分回执](../notes/r150-infinity-remote-session-789f/43702348535-selected-natural-second-left-normal-four.json)实际得到
$$
\operatorname{rank}_{\mathbb F_{31}}\overline H_4=1355,
\qquad
\det\overline U=25\ne0
\tag{1.2}
$$
于所选原1355阶单位块 $U$，并保存完整 $M_4$ 和原行列剖面。首次入口只因自设64列限制停在该前缀；它没有产生有理核结论。

## 2. 全部130个右端及完整高Schur

续接固定这个实际剖面，不重构 $M_4$，不重作模素数消元。将130个实际自由列按
$$
32+32+32+32+2
$$
分批，逐批求原单位方程的完整有理解。每列清分母为整数图向量 $v_j$：其自由坐标为正整数 $D_j$，主坐标为完整分子 $N_j$。每批返回后立即保存全部数值及哈希，尚未作全高行乘回时仍只标候选。

对全部原1736行形成
$$
S_{\rm high}=H_4[v_1,\ldots,v_{130}].
$$
本次实际有理Schur增秩为零。将列逐一原始整数化得到
$$
Z_4\in\mathbb Z^{1485\times130}
$$
并实际核验
$$
\boxed{H_4Z_4=0}
\tag{2.1}
$$
于全部 $1736\cdot130=225680$ 个原坐标；同时核自由坐标像秩恰为130。因此 (1.2) 给下界1355，(2.1) 给上界 $1485-130=1355$，得到
$$
\boxed{
\operatorname{rank}_{\mathbb Q}H_4=1355,\qquad
\ker_{\mathbb Q}H_4=\operatorname{im}Z_4,\qquad
\dim\ker_{\mathbb Q}H_4=130.
}
\tag{2.2}
$$
这个结论使用完整高Schur和全部原行，不是把有限域核直接提升。

## 3. 回到原第二连接：130个校正如何使用

完整新方程为
$$
M'_0x+R\theta+M_4\eta_4=0.
$$
由1736个高行及 (2.2)，它等价于存在 $\alpha\in\mathbb Q^{130}$ 使
$$
\eta_4=Z_4\alpha,\qquad
M'_0x+R\theta+W\alpha=0,\qquad W=M_4Z_4.
\tag{3.1}
$$
仍须保全部4354原行。旧单位块已付的36个解和全部旧残差可以直接复用；只需新求 $W$ 对应的130个单位右端。

令 $P$ 是旧1546个单位行，$U_0=(M'_0)_P$，定义完整消去算子
$$
\mathcal E(v)=v-M'_0U_0^{-1}v_P.
$$
则 $\ker\mathcal E=\operatorname{im}M'_0$。置
$$
S_{\rm old}=\mathcal E(R),\qquad S_{\rm new}=\mathcal E(W).
\tag{3.2}
$$
原旧残差可能逐列乘了已保存的非零整数分母；这些缩放不改变其列空间，恢复原 $\theta$ 时必须带回原分母。

[完整同选常左核](R150-appendix-selected-exact-cokernels49-36-and-natural-schur-interface.md)已证明常左核在normal次数 $\ge3$ 的坐标上为零。旧 $M'_0$ 的校正嵌入支持normal≤3，且 $M'_0$ 列满秩。因此，若 $W\alpha\in\operatorname{im}M'_0$，则
$$
(A_0)_{I,J}^{\mathsf T}(E_4Z_4\alpha-E_{\rm new}x)=0.
$$
取normal4分量即得 $Z_4\alpha=0$，进而 $\alpha=0$。故
$$
\boxed{\operatorname{rank}S_{\rm new}=130.}
\tag{3.3}
$$

旧 $S_{\rm old}$ 秩为14。令
$$
\iota=\dim\bigl(\operatorname{im}S_{\rm old}
                   \cap\operatorname{im}S_{\rm new}\bigr).
$$
则
$$
\operatorname{rank}[S_{\rm old},S_{\rm new}]=144-\iota,\qquad
\dim\ker[S_{\rm old},S_{\rm new}]=22+\iota.
\tag{3.4}
$$
该联合核向原33维 $c$ 的投影仍单射：若 $c=0$，则原第一连接恰为3迫 $t=0$；随后 (3.3) 及 $M'_0$ 列满秩迫 $\alpha=x=0$。所以normal≤4的真实二阶头维数恰为 $22+\iota$。原第二连接下界9又给
$$
\boxed{0\le\iota\le2,\qquad
142\le\operatorname{rank}[S_{\rm old},S_{\rm new}]\le144.}
\tag{3.5}
$$
本次尚未求 $S_{\rm new}$ 的完整数值，也没有决定 $\iota$。只有后续实际得到24个独立原头并核全部4354产品，才可宣布完整第二连接恰为9。normal5仍未排除。

## 4. 真实运行、输入绑定和可恢复输出

首次normal4实际运行与续接都在run43702348535。续接步骤为selected-natural-second-left-normal-four-continue，执行源码提交c8d76ff9c19e248f9a2809bbef1ff06fc3b5d0ac。

[续接源码](../notes/2026-11-15-r150-selected-natural-second-left-normal-four-continue-789f.py)的SHA256为：
~~~
eabfa9bb969b4e62afbeb21b18f3f662da3606a5bf894790beef55f65c7e278d
~~~
准确参数与全部固定输入见[续接接口](../notes/2026-11-15-r150-selected-natural-second-left-normal-four-continue-interface-789f.md)。共享数学预算300秒、每进程2048MiB；实际数学21.356861559秒、墙钟21.423979823秒。高核阶段实际20.820643471秒，五批130个右端全部完成。

新绑定为c18a0a21f0ca0e44aeaa65c138bbf02e5b26fc7d01542573aef47dbc7b532fec，显式保原前缀绑定8b3f9574b5fa816b6f967bc9c9530c6dc991e879f070964d0d409b360ffad781。

| 完整临时对象 | 字节数 | SHA256 |
|---|---:|---|
| 全部高单位有理候选 | 1437630 | e827223af4eec51f919e2e765fdf5738e45fe7caacdd5d09b51d432aefd5ad9c |
| 完整130列原高核 | 1446855 | 46b047a303d68a3502aa076836f77dc0fde101ca93d6df2c8568380f2d190d63 |

完整小回执5667字节，SHA256为161e2a48e5b82fd26c67a9100b95e75b88ce85ecb395eb59dc84a760c637aa34。[已推实际回执](../notes/r150-infinity-remote-session-789f/43702348535-selected-natural-second-left-normal-four-continue.json)保存全部输入、完整高核状态和实际各阶段。

程序在高核已完整核验后，因后半旧辅助worker的64列形状上限返回退出码75及completed-prefix/actual-high-kernel-needs-wider-next-worker。这个状态不减损 (2.2)，也不表示完整第二连接已完成。后继直接消费该真130维高核，只新增130个辅助单位右端；不重算高块、剖面、高核或旧36个单位解。所有可重算大数组仅留本次临时会话。
