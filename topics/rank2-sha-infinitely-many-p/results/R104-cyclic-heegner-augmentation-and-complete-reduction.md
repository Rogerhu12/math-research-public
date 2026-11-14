# R104. 实际循环增广商与完备好约化证书

## 好约化位提供完备检测

Creutz–Lu 的 split CM 定理适用于本题全部目标 $p$，且对任意数域
$L$、任意 $M\ge1$ 都有完整 $H^1(L,E[p^M])$ 的局部核为零，
允许删去任意有限位集合。因此对实际点 $R\in E(L)$，
\[
R\notin p^ME(L)
\iff\exists\text{好位 }v\nmid p:
\bar R\notin p^M\widetilde E(k_v).
\]

对 $L=F[\ell]$，还可以直接证明：在 $p,2$ 不分歧保证 Galois 像
是完整 split Cartan 正规化子，阶 $2\varphi(p^M)^2$。
中心元素 $-I$ 的 Sah 论证给 $H^1(G,E[p^M])=0$。
若 $R$ 不可除，其在挠点域上的 Kummer 平移群 $W$ 非零；
Chebotarev 给完全分裂于挠点域的证书位，其密度准确为
\[
\frac{|W|-1}{2|W|\varphi(p^M)^2}>0.
\]
这没有在证明不可除之前就保证某个位成功；非零 $W$ 是必要输入。

## 真实点群缩到次数 p^M 的循环域

额外取 $\ell$ 在 $\mathbb Q(i)$ 惰性，排除 $p\mid h_F$，写
$\ell+1=nu$、$n=p^M$、$p\nmid u$。
对 $\Gamma=\operatorname{Gal}(L/F)=\Gamma_p\times A$，
$|\Gamma_p|=n$、$|A|=h_Fu$，令 $L_p=L^A$ 并取实际整数迹
\[
Q_{\ell,p}=\operatorname{Tr}_{L/L_p}P[\ell]\in E(L_p).
\]
它满足 $N_nQ_{\ell,p}=0$。若 $\tau$ 生成 $\Gamma_p$，
$D_n=\sum_{j=1}^{n-1}j\tau^j$，则准确有
\[
Y_\ell\equiv D_nQ_{\ell,p}\pmod{nE(L)}.
\]
由于 $[L:L_p]$ 与 $n$ 互素，res/corestriction 给
$E(L_p)/n\hookrightarrow E(L)/n$，没有除以群阶来虚构一个点。

令 $\mathcal M=\ker(N_n:E(L_p)\to E(F))$。
利用 $E(L_p)[p]=0$ 和 $(\tau-1)D_n=n-N_n$，得到
\[
\boxed{Y_\ell\notin nE(L)
\iff [Q_{\ell,p}]\ne0\text{ 于 }\mathcal M/(\tau-1)\mathcal M.}
\]
这是实际有限整数增广商；仍只在所选辅助素数子族给充分证书，
没有将 R100 的全部必要性收窄到此子族。

## 范数点与可能的 Sha 分量都保留

有准确短正合列
\[
0\to\frac{N_nE(L_p)}{nE(F)}
\xrightarrow{[N_nZ]\mapsto[(\tau-1)Z]}
\frac{\mathcal M}{(\tau-1)\mathcal M}
\to H^1(\Gamma_p,E(L_p))\to0.
\]
正文构造完整下降 cocycle；其 Weil–Châtelet 像为
上述右端类的负 inflation。
若实际 $Q_{\ell,p}=(\tau-1)Z_0$，下降类准确等于
$-\delta_n(N_nZ_0)$，从而接回基域已知点的 Kummer 比较。
否则保持真实的 Sha 分量，未先假定它为零。

[完整证明、符号及来源](../notes/2026-11-12-cyclic-heegner-augmentation-and-complete-reduction.md)
已由根端全文独审；Creutz–Lu 的定义与主定理已亲读。
仍待证明：随 $p$ 变化的真实 $Q_{\ell,p}$ 在指定增广商内对无穷多个
$p$ 非零。原 Heegner 点不可被 $p$ 整除尚不提供这个结论。
