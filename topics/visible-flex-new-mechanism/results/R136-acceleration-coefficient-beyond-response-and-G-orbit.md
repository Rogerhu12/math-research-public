# R136：完整加速度系数给出超出全部响应与 G 轨道的真实第四成本方向

日期：2026-11-14。**已证明；只消费一次新的公开实际。**

记 $R=\mathcal R_8$、$U=\mathcal U_4$，并令

$$
A_G=R+\operatorname{span}\operatorname{Orb}(G).
$$

本次从 R134 的完整加速度层取出一个实际属于 U 的真权 −2 系数 J，并用 41/42 阶原有理子式证明

$$
\boxed{
J\in U_{-2},\qquad
J\notin R_{-2}+\mathbb RN^3G,\qquad
J\notin A_G.
}
\tag{1}
$$

因此

$$
\boxed{U/A_G\ne0,\qquad \dim U\ge r+s+1,}
\tag{2}
$$

其中 $r=\dim R$、$s=\dim(A_G/R)$。仅合并已经发表的 R135 即有 $\dim U\ge152$。这个新维数属于真实 **span**；它没有自动增加闭锥 lineality 或已能有限联合支付的查询数。

## 1. 唯一实际与冻结输入

公开实际为 [run 43654534244](https://github.com/Rogerhu12/math-research-public/actions/runs/43654534244)，source

~~~text
1177f251dc3d9455adf88b585e4c0e4bd6f7e69b
~~~

lane 为 acceleration_layer_mixed。驱动 [literature_acceleration_layer_mixed.py](../scripts/literature_acceleration_layer_mixed.py) 为 47656 B，SHA256

~~~text
271dd150fe95d280fdf3cad0f5bbb5b5fde6f81631a96e7fdbfeb628711ebf7c
~~~

研究正常 complete，耗时 **18.34833271499997 秒**，峰值 RSS **255.16015625 MiB**。不是资源退出。此前同 job 的 13 项人工接口检查全部通过；实际开发回执耗时 0.0018870139999762614 秒。

[主报告](../notes/actions-43654534244-1-acceleration_layer_mixed/acceleration-layer-mixed.json)为 57753 B，SHA256

~~~text
baccbf48f39a7fb3296ca4e8a933d18f246a8db317423846e66d9c46374b2745
~~~

[发布回执](../notes/actions-43654534244-1-acceleration_layer_mixed/receipt.json)为 35241 B，SHA256

~~~text
3c147ca2edaa03d4c27fa0694adca26764c0f98c8fde363387359d8fddccc494
~~~

完整结果和新原式均已发布：

| 内容 | 字节数 | SHA256 |
|---|---:|---|
| [完整数学报告 gzip](../notes/actions-43654534244-1-acceleration_layer_mixed/acceleration-layer-mixed-complete-report.json.gz) | 43071 | af242f353bfb3e038615a8bc1f9d28752b75233be58f7f1a8ad8f89713110891 |
| 上行解压 JSON | 175927 | a106c8a0162ef7c51ca8ad03546ef2d7607f2dabe34a00169acad97c9ed9c9b4 |
| [五族完整原式 gzip](../notes/actions-43654534244-1-acceleration_layer_mixed/acceleration-layer-mixed-original-expressions.json.gz) | 318634 | b3227509c891a2e86e9bcc7823e3d6b3abb0a9ff80975b2e1162a0911739146e |
| 上行解压 JSON | 1909429 | 7c1e0bda999d2c8958d7e5fdf6d9460f30eb6003eb1c69172ba1ca948dfeac38 |

[公开人工主回执](../notes/actions-43654534244-1-acceleration_layer_mixed/acceleration-layer-mixed-development.json)为 8491 B，SHA256 a5bc9f31c3e08fd3d167afd7e2760d91afd6d8c081cf129c0a2b26f56010f80e。该人工回执没有计算研究目标。

两份输入是：

1. run 43651096112 / source 2259b57065cfad67682f4c4319885fd5334c4f76 的完整变量几何因子。原 gzip 2132064 B / 9daddeaf6ad8e7aa647df4f8084ec803625c589bfc51f595ff0d9c680ce0dd4a，原始 11864540 B / 58e450c47123fc682f665fffb2bb66829d9d37f502b7163e2875089b72f93fd3。
2. [R131](R131-third-G-translation-separation-and-111-query-control.md) 的已完成新权块：run 43653293263 / source 2f0add61f44365d713abf836beaa8b0be2806a3d，50 列完整原式 gzip 157782 B / 226ea60c21cac82674cd58df491e554eb226431953f4306f0c2c630e1228358e。

主报告、生产者、终端发布 receipt、压缩及原始哈希全部绑定。没有重编 forcing、变量局部生成器、W36 或旧响应组合，也没有重新推导 R131 的十条原式依赖。为新的 42 阶子式，只共同评价已经保存的 41 个原控制和一个新目标。

## 2. 五个真实正规族与新系数 J

[R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md) 的完整最高几何导数层为

$$
L_4=D_sP_3+
\bar A_{hh}a^2+\bar A_{hk}ab+\bar A_{kk}b^2
+(H_1u+H_2w)(ub-wa)+\widehat Q_4,
\tag{3}
$$

其中 $u=h_s,w=k_s,a=h_{ss},b=k_{ss}$，真实约束是 $\omega_s=k_s/(2h)$。

[R134](R134-acceleration-layer-from-complete-local-v4.md) 证明五族 $\bar A_{hh},\bar A_{hk},\bar A_{kk},H_1,H_2$ 只需完整 $v_4$ 的加速度和三阶导数项。$m_2,N_2$ 为速度二次，所以 $B_{m_2}N_2$ 只改速度四次层，不能把 N₂ 从整个 L₄ 丢掉，但无需为本五族形成 N 响应。

本次从每个模式的 1236 个原 $v_4$ 系数中消费 906 个加速度/三阶项，另外 330 个速度四次项显式留待后续。全部真实状态导数

$$
X=\partial_h,\qquad
Y=\partial_k+\frac1{2h}\partial_\omega
$$

以及 Laurent/log 链式项保留。总共得到 **314 个未分权状态系数**，同一实系数同时作用于完整 $-4,-2$ 两模式。

令 $\Pi_{-2}$ 表示真实 profile 缩放权 −2 投影，定义

$$
\boxed{
J=
\Pi_{-2}\!
\left(
[h^{-4}k^0\omega^0(\log h)^0]\bar A_{hh}
\right).
}
\tag{4}
$$

方括号是状态 Laurent/多项式系数提取，不是某个任选静态点的采样。报告 candidate 0 的别名恰为 A_hh，state_key=(-4,0,0,0)，状态顺序是 $(h,k,\omega,\log h)$。

由 [R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)，五族实际状态值的 span 属于 U。独立 Laurent/log 状态单项的系数也属于同一有限真实 span；再由 R105 的真实缩放不变性取权投影，故

$$
J\in U_{-2}.
\tag{5}
$$

这里没有先假定几何系数可各自任意有符号调节。使用的是已证明的真实 **span 等式**。

J 的完整两模式原式 SHA256 为：

| 模式 | 原式 SHA256 |
|---|---|
| $-4$ | 2efefe7d9d902bb0050e4f19fc16b09060216c2376530d920ef265ee9ce96ad3 |
| $-2$ | 70f565c5c6d7075ec99bc383fc0ee66e914aff06fbc273bc3c1e431123d7c979 |

## 3. 唯一被研究的权块与真实控制上界

新五族的真权 −2 系数分布为：

| 族 | 真权 −2 状态系数数 |
|---|---:|
| $\bar A_{hh}$ | 4 |
| $\bar A_{hk}$ | 2 |
| $\bar A_{kk}$ | 1 |
| $H_1$ | 2 |
| $H_2$ | 1 |

原式去同后恰有 10 个目标。本次代表拟合对 10 个均未给成员身份；这十个非零 word 余项**没有**被当作十个函数非成员证明。驱动按冻结设计只选第一个 J 作一次原式有理分离，其余九个仍未决。

R131 已证明

$$
\dim R_{-2}=40,\qquad N^3G\notin R_{-2}.
$$

消费者读取其全部 50 列原式，核完整 E8×W36 的顺序、原哈希和已完成上界，取以下 40 个保留原列：

~~~text
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,
20,21,22,23,25,27,28,29,31,32,33,35,36,39,40,41,46,47,48,49
~~~

并加第 41 列 N³G。这些列的真实 span 正是

$$
A_{G,-2}=R_{-2}+\mathbb RN^3G,
\qquad \dim A_{G,-2}=41.
\tag{6}
$$

理由不依赖尚未完成的更高 G 链：G 自身纯权一，平移幂依次为 $1-j$，缩放仅乘相应正幂；因此整个仿射轨道的权 −2 部分只可能由 N³G 张成。没有任何其他 profile 权可以在真直和分解中抵消 J。

## 4. 41/42 阶原有理分离

取 R131 同一个实测试对

$$
f=t^8(1-t)^8,\qquad
g=f(1+2t+3t^2+5t^3),\qquad
q=f+ig,\qquad t=\xi-2\in[0,1],
\tag{7}
$$

在外侧零延拓，共同右锚为 3。实际输入最高 jet 为 4；$C^7$ 延拓足够定义评价，并允许保持所需 jets 与积分连续性的光滑逼近。没有声称这个未经补偿的测试对已经是三矩圆。

原式评价器在 $t=j/25,\ j=1,\ldots,24$ 取两模式实/虚，共 96 行，顺序为每个 j 的 $-4$ 实、$-4$ 虚、$-2$ 实、$-2$ 虚。它直接评价原 Volterra 积分，没有评价 word 余项。

令 A 为 (6) 的 41 列有理矩阵，b 为 J 的评价列。控制行集为

~~~text
Jrow = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
        18,19,22,23,26,27,30,31,34,35,38,39,42,43,46,47,
        50,51,54,55,58,59,62,63)
~~~

额外行 $e=66$，即 $j=17,-2$ 实部。控制行恰为 R131 的 41 条增广行，新增一列/一行完成本轮子式。

检查过的素数 $p=2147483647$ 下，

$$
\det A_{\rm Jrow}\equiv64963154\ne0\pmod p,
$$

$$
\det
\begin{pmatrix}
A_{\rm Jrow}&b_{\rm Jrow}\\
A_e&b_e
\end{pmatrix}
\equiv602105349\ne0\pmod p.
\tag{8}
$$

全部 81 个遇到的有理分母均可逆，最高实际多项式次数为 74。完整 42×42 模矩阵在数学 gzip 中，规范 SHA256 为

~~~text
f0965e518249763e99e4d9770831bf147db401be9fc4bfe73c389e6cb7f307e5
~~~

定义真正的有理泛函

$$
\Lambda_0(V)=\operatorname{ev}_e(V)
-A_e A_{\rm Jrow}^{-1}\operatorname{ev}_{\rm Jrow}(V).
\tag{9}
$$

由定义，所有 41 个原控制的值在 $\mathbb Q$ 上严格为零；目标则满足

$$
\Lambda_0(J)\equiv134118430\ne0\pmod p.
\tag{10}
$$

打印的模 p 系数不能直接当作 (9) 的有理系数。非零模值只证明非零，不给实数符号。原有理子式的合法非零约化证明

$$
J\notin A_{G,-2}.
\tag{11}
$$

由于 J 纯权 −2，而 $A_G$ 在真实仿射表示下分权，(11) 严格推出 (1) 的完整非成员，不依赖正规形完备性。没有据此宣称 (9) 在固定测试对上还杀掉所有其他权的评价列。

## 5. 完整商已经超出 R 与整个 G 轨道

(5)、(11) 给

$$
\boxed{\dim U/A_G\ge1.}
\tag{12}
$$

所以“继续 G 的平移链最终就能张成全部 U”不成立：即使 G 的尚未确定后继全部计算完成，J 仍在完整轨道之外。后继 G 链对其自己的可调子空间和维数仍有用途，本结果不把它们改成无效证据。

令 $r=\dim R,\ s=\dim(A_G/R)$，则

$$
\boxed{\dim U\ge r+s+1.}
\tag{13}
$$

例如 [R135](R135-fourth-G-translation-separation-and-151-query-control.md) 已给 $r\ge146,\ s\ge5$，所以仅合并那一已经发表的界即得

$$
\dim U\ge152.
\tag{14}
$$

本稿不把 (13) 的额外 1 自动加到 lineality 或 R122 的实际查询支付数中。R130 证明 J 属于真实成本的线性 span，未证明可在固定基准上取任意正负倍 J。R137 的完整 PSD 必要门正可用于进一步检查其可能正性，而不能被本次模素数非零替代。

## 6. 为什么 pure m=8 尾看不到这个新方向

[R133](R133-complete-m8-pure-cost-range-and-exact-tail-payment.md) 已证明完整 pure 尾投影满足

$$
\Pi_8(U)=\Pi_8(R).
\tag{15}
$$

所以 J 的该 pure 投影必在已付响应像中，尽管 (1) 在完整两模式原式中严格成立。这不是冲突：$\Pi_8$ 有核，且它把所有完整商信息在这个测试层都消掉了。

因此本结果不要求再跑 m=8 尾来猜 J 的完整成员性，也没有从同一单测试 profile 外推所有合法圆都被这个 J 阻塞。

## 7. 新导出可直接复用

新导出 scope 为 five-complete-two-mode-normal-acceleration-families，含：

- 全部 314 个未分权状态系数的 628 个两模式根；
- 10 个新真权目标的 20 个两模式根；
- 总计 648 个根、1917 个 profile 原子、79291 个根单项；
- 状态顺序、五族标签、原哈希、真权别名、两个输入的完整来源绑定。

此后检查其他权、同权其他九个目标或真实正性结构，可以直接消费这些原式；无需重新提取完整 $v_4$、构造 N 响应或重编旧 forcing。

这只是复用入口，不授予未经研究的其他九项非成员、五族准确总秩、完整 U 维数或新的 finite control 可达结论。

## 8. 仍未完成

完整 P₀ 函数与 ruling 的同付、双 collar、高阶和收敛、非平凡有限等距族以及闭嵌入、reach、握持区和宏观位移，仍须继续处理。本次支付的是一个明确的完整成本新方向及其可核原式证书。
