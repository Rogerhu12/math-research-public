# R150：第三页完整三次横向校正的二维合法核

日期：2026-11-15 UTC。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

本稿固定已经支付的原无穷远十三个二阶左 jet，完整加入次数至多五的全部三次横向三阶校正。其高来源合法性条件的核准确为二维；尤其所有总次数五的三次横向校正系数都被迫为零。两条合法列并入原低来源后，第三页残差仍增秩一，leading 可延拓空间仍为原前十二个方向。

这是这个完整三次横向校正范围的结论，不是完整第三连接的秩一下界。四次、五次横向校正仍未排除，原 $\operatorname{rank}\beta_{3,\infty}\le1$ 与公共 $43/39$ 阶保持不变。

## 1. 固定原来源和已付二阶规范

使用[原第三页证明](R150-appendix-infinity-third-connection-one-dimensional-bound-order43-and-cost8663.md)
的全部 $6188$ 个来源、自然参数 $u=1/s$、物理反序及完整共动变换。
写 $c=n_0,d=n_1,z_j=n_j$，$2\le j\le10$。常项原十七式有分解
$$
F_{0,i}(c,d,z)=
\sum_{l=2}^{10}\bigl(\ell_{i,l}+c\,b_{i,l}+d\,a_{i,l}\bigr)z_l
+\sum_{2\le j\le k\le10}q_{i,jk}z_jz_k.
\tag{1.1}
$$
纯切向常项严格为零，原式总次数至多二。

保持已付十三条二阶左 jet
$\Lambda_0+u\Lambda_1+u^2\Lambda_2$，
其中 $\Lambda_1$ 最高一次横向、$\Lambda_2$ 最高二次横向。第三残差
$$
R_3=A_3^{\mathsf T}\Lambda_0+
A_2^{\mathsf T}\Lambda_1+
A_1^{\mathsf T}\Lambda_2
$$
只支持原 $1088$ 个零次、一次横向来源行。前稿保同一 $J_0,J_1=A_1^{\mathsf T}Q$，
并给
$$
\operatorname{rank}J_0=578,\qquad
\operatorname{rank}[J_0,J_1]=582.
\tag{1.2}
$$

## 2. 三次横向校正的全部高来源约束

允许额外三阶校正 $\eta$ 支持全部
$$
c^ad^bz_iz_jz_k,\qquad a+b\le2,\quad 2\le i\le j\le k\le10.
\tag{2.1}
$$
共有 $6\binom{11}{3}=990$ 个坐标。

恰含两个横向变量的原来源为
$$
c^ad^bz_jz_kF_i,\qquad a+b\le1,\quad 2\le j\le k\le10,
\tag{2.2}
$$
共 $17\cdot3\cdot45=2295$ 行。在这些行上，原 $R_3$、$J_0$ 和 $J_1$ 都为零，而
$A_0^{\mathsf T}\eta$ 等于
$$
(\mathcal H_3\eta)_{i,a,b,j,k}
=\sum_l\left[
\ell_{i,l}\eta_{a,b,\operatorname{sort}(j,k,l)}
+b_{i,l}\eta_{a+1,b,\operatorname{sort}(j,k,l)}
+a_{i,l}\eta_{a,b+1,\operatorname{sort}(j,k,l)}
\right].
\tag{2.3}
$$
因此合法性必须且只需满足
$$
\boxed{\mathcal H_3\eta=0,\qquad
\mathcal H_3\in\mathbb Q^{2295\times990}.}
\tag{2.4}
$$
这里完整保留了 $(c,d)$ 乘一次横向变量的二次项；不能仅由
$\sum_l\ell_{i,l}v_l=0$ 将原三次求值泛函随意乘 $c$ 或 $d$。

其余 $2805=17\binom{11}{3}$ 个来源含三个横向变量。由于 $F_0$ 至少一次横向，
这些来源输出至少四次横向，对 (2.1) 恒为零。故 (2.4) 保全部原高来源，没有删除边缘次数的条件。

## 3. 实际完整核及其次数定位

按总切向次数 $0,1,2$、随后 $a=0,\ldots,a+b$ 和升序三元组排序 (2.1)。
实际精确有理消元给
$$
\boxed{\operatorname{rank}\mathcal H_3=988,\qquad
\dim\ker\mathcal H_3=2.}
\tag{3.1}
$$
规范核矩阵 $N\in\mathbb Q^{990\times2}$ 满足
$$
\mathcal H_3N=0
$$
的全部 $2295$ 行；自由坐标准确为零起始索引 $164,494$，即
$$
z_{10}^3,\qquad cz_{10}^3.
\tag{3.2}
$$
其两行规范为 $I_2$。

特别，总切向次数二的全部坐标索引为 $495,\ldots,989$。这些都是排在最后自由坐标之后的 RREF 主元，因此任意核向量在这些坐标上严格为零：
$$
\boxed{
\eta_{a,b,i,j,k}=0\quad\text{只要 }a+b=2,\quad
\eta\in\ker\mathcal H_3.}
\tag{3.3}
$$
所以完整合法三次横向校正事实上只用总次数三、四，没有总次数五的分量。这是实际全高来源约束的结果，而非预先缩小校正空间。

此前单列候选在纯三次横向齐次部分以固定 $v$ 求值。
算法准确核 $\ell_i(v)=0$，并验证其完整 $990$ 坐标列属于 $\operatorname{Ran}N$，规范自由坐标为 $(1,0)$；所以该候选准确等于 $N$ 的第一列，没有在本次扩展中丢失。

## 4. 两条合法高列的真实低来源作用

三次横向校正在纯来源上为零。在一次横向来源
$c^ad^bz_lF_i$、$a+b\le2$ 上，准确作用是
$$
(\mathcal K_3\eta)_{i,a,b,l}
=\sum_{j\le k}q_{i,jk}
\eta_{a,b,\operatorname{sort}(j,k,l)}.
\tag{4.1}
$$
记
$$
\mathcal K_3\in\mathbb Q^{1088\times990},\qquad
E_3=\mathcal K_3N\in\mathbb Q^{1088\times2}.
$$
完整高核消去以后，第三阶校正问题准确变为
$$
[J_0,E_3,J_1,R_3]
\begin{pmatrix}H\\C\\B\\Z\end{pmatrix}=0.
\tag{4.2}
$$
反向也成立：任何合法三次横向 $\eta$ 都是唯一的 $NC$，故 (4.2) 没有遗漏这个校正范围的任何候选。

实际三个前缀秩为
$$
\operatorname{rank}[J_0,E_3]=580,\qquad
\operatorname{rank}[J_0,E_3,J_1]=584,
$$
$$
\boxed{\operatorname{rank}[J_0,E_3,J_1,R_3]=585.}
\tag{4.3}
$$
十三个 leading 方向的可延拓空间仍准确为
$$
Z=\begin{pmatrix}I_{12}\\0\end{pmatrix}.
\tag{4.4}
$$
全部低 $1088$ 行乘回和高 $2295$ 行核身份同时成立；另外 $2805$ 行由横向次数恒零。两条新合法列虽然分别增大了 $A_0^{\mathsf T}$ 的校正像，但没有升起最后一个 leading 方向。

由这些身份可构造真实左 jet
$$
\Lambda_0Z+u\Lambda_1Z+
u^2(\Lambda_2Z+QB)+u^3(H+NC).
$$
这里 $H$ 和 $NC$ 嵌入互不重叠的目标次数块。再按原目标变换的转置运输，仍保全部原来源。

(4.3) 只排固定已付二阶规范、允许全部一次至三次横向三阶校正的该扩展问题。它没有排四次、五次横向校正，也没有证明完整 $\beta_3$ 存在非零真实来源。因此不增加或减弱前稿的全连接上界及来源费用。

## 5. 实际记录、临时检查点与复现

[小源码](../notes/2026-11-15-r150-infinity-third-complete-cubic-normal-kernel-789f.py)
SHA256 为
42f91004ab4cbd248e7856902bb190ebf3a80fcb43cfe20a7bec27232c49791c。

实际运行 $43702348535$，步骤 infinity-third-complete-cubic-normal-kernel，
执行源码提交 db2d7f2d63afe7ac110e91e61ed28f5c1b8905dc。
数学限额 $30$ 秒，实际内存限额 $512$ MiB；
数学用时 $6.005971283000008$ 秒，退出码 $0$。

| 对象 | SHA256 |
|---|---|
| 完整高来源矩阵 $\mathcal H_3$ | 7fd74db4de1319745b0a51ba259974e25a0a8d9887a2022a107bdb620801b221 |
| 完整二维核 $N$ | c10632a05ab35246f09f7595d090c54d533d010c5fbded2c23f5958dbe523464 |
| 合法低来源像 $E_3$ | 77f4d0e7ee46c52d107ba01c062861907747c64be7c95291905da0c6da986044 |
| 完整低 $1088\times607$ 增广矩阵 | da890b6dbf946d006a412fdea1a51fb2924270bd3c70bf9c9afdf89469643847 |
| 完整三阶校正 | cae91171d51f8292056fe5e46dcc261927d185592928411666d51e8a95ab57f5 |

高核和低像先后保存到同作业的临时、按内容寻址检查点，绑定源码及全部小输入的 SHA；中断可只续未完成的小步骤。两矩阵压缩检查点分别为 $12240$ 与 $13150$ 字节，未上传或提交。只长期保留源码、参数和小回执。

原小回执 $10185$ 字节，SHA256 为
d15ab639458733b787ed1270c51db61e8d9118505c34ef5aa101a6424202c1eb。
[实际执行记录](../notes/r150-infinity-remote-session-789f/43702348535-infinity-third-complete-cubic-normal-kernel.json)
保完整输入绑定、高核自由坐标、全部 $3383$ 非自动来源与 $2805$ 自动来源的身份、实际秩及临时检查点哈希。
