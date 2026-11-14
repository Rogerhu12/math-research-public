# R119：全模式真线性中心及同一个低 46 模真解的更小修正球

作者：/root（GPT-6 Astra Pro；AI-assisted），2026-11-13。

**已证明并实际执行。** 在 R100 原完整单位参数域上，同一个 R105 低 46 模真实投影解，以全部 20 个非零模式的真实线性场为中心，满足

\[
\boxed{\|Y-L_R\|_X<1.31\times10^{-13}.}
\]

这里的度规、两胞元的原 10793 个材料叶、全部 10878 个真实几何子片、外端目标和内头完整非线性迹均未改变。只是把原混合中心的已知线性差移回中心本身。下面的实际计算保留完整 mean 根、逆分母余项和全部 46 个非零输出。它尚未支付 46 个切口参数的一致性、全频外方程或完整闭曲面。

## 1. 同一个问题和新的固定中心

沿用 R87/R90 的实际无迹物理列及同一真实 Wronskian。对每个正偶数 \(m\le92\)，令

\[
\lambda_m=Q_m^{\mathrm{out}}/S^0_{Q,m},\qquad
L_{R,m}=(P_m,K_m)=F^{-1}\phi_m\lambda_m,
\quad F=\sqrt{rw^3}>0.
\tag{119.1}
\]

原外端目标只有 \(m=2,4,\ldots,40\) 非零，故其余 26 个中心模式准确为零。\(S^0_{Q,m}\) 是原真实内头线性斜率对应的外端高度列，不是有限 Robin 替代物。原数据已为全部 46 个分母和 Wronskian 排除零。本次读取并逐文件核对其完整有符号区间。

R105 的中心只在 \(m=2,4\) 使用此真实线性列，其余 18 个非零模式仍取旧候选。新的 (119.1) 在所有模式均为同一个 \(L_R\)。因此在投影固定点恒等式

\[
Y=L_R+\mathcal B\beta(a)+\mathcal G\Pi_{46}\mathcal N(Y)
\tag{119.2}
\]

中，仿射中心差 \(L_R-Z\) 现在准确为零。参数 \(a\) 只通过原真实内头非线性迹 \(\beta(a)\) 进入此恒等式；中心本身不依赖 \(a\)。没有把旧候选的误差删掉，也没有替换原方程。

使用 R90/R105 原局部包络 \(V(x)>0\) 和 \(\sigma=1/64\)，定义

\[
\|Z\|_X=\sum_{m=2,4,\ldots,92}(1+m)e^{\sigma m}
\left(\sup_x|P_m(x)|/V(x)+\sup_x|K_m(x)|/V(x)\right).
\tag{119.3}
\]

每模每分量的径向 supremum 都在求和之前取。实际全叶计算给

\[
\|L_R\|_X\le7.026685781247125\ldots<8.
\tag{119.4}
\]

## 2. 全部真实材料上的完整源

新入口 `root_outer_full_linear_centre_source.py` 不复用旧中心的 mean 或源值。它在每个原材料叶对应的每个真实几何子片上，由 (119.1) 重新构造全部 20 个物理 Fourier 系数，并使用原 \(r,r_x,w,\ell=(\log w)_x\)。所有原 source 包络 \(V\)、区间端点和相邻覆盖均逐项核对。

令 \(s=r_x/r\)、\(c_{\rm bg}=s+|\ell|\)，用 R109 的准确 Laurent 公式构造

\[
\mathcal N_4=\Pi_\perp A_2(1-l_2+l_2^2-l_2^3).
\tag{119.5}
\]

其中二次 mean \(c_2\)、它在分子中的全部交叉项、二次零频率与完整有限乘积都保留。没有在乘积中间投影到 46 模。最后才读取全部 46 个 cosine 系数。

R109 式 (109.10) 已证明，在任一合法角条带 \(\tau\) 上，若物理强范数 \(R_\tau\le1/64\)，则

\[
\|\mathcal N-\mathcal N_4\|_{\tau,0}
\le681c_{\rm bg}R_\tau^4.
\tag{119.6}
\]

它包含完整 mean 小根的替换误差和完整逆分母的剩余项。本次每行分别核对 \(\tau=\sigma\) 及 \(\tau=\log q\)、\(q\in\{2,4,8,16\}\) 的半径。只对已经严格通过域门的 \(q\) 使用其输出系数界。因此第 \(m\) 个 cosine 余项界可取

\[
\epsilon_m=681c_{\rm bg}\min\{R_\sigma^4e^{-\sigma m},\ R_{\log q}^4q^{-m}:R_{\log q}<1/64\}.
\tag{119.7}
\]

正负系数的相等来自原 parity；paired Wiener 质量已经包含两个 Fourier 半幅，所以 cosine 界没有再添加或漏掉因子 2。未通过较宽条带域门的选择被丢弃，原 \(\sigma\) 完整界始终保留。

实现把 (119.5) 的有符号区间与 \([-\epsilon_m,\epsilon_m]\) 相加。每一个系数、余项和后续正上界均显式检查 finite；不存在把 NaN 交给 `max` 后静默忽略的路径。此源值计算只乘正材料界，不将宽 \(s+|\ell|\) 区间作为分母。

## 3. 有符号切口积分和整个径向区间的响应

每个几何子片 \(I\) 上，由已认证的真实列直接包围

\[
I^\phi_{I,m}=\int_I\phi_{1,m}F\mathcal N_m(L_R)\,dx,
\qquad
I^\chi_{I,m}=\int_I\chi_{1,m}F\mathcal N_m(L_R)\,dx.
\tag{119.8}
\]

带符号的实际列、\(F\)、完整源和准确片长相乘，给整个子片的合法区间。各完整贡献向外舍入为明确的 dyadic 端点；全域和在准确有理数中累加。保存的切口量是

\[
Q_m^{\rm fixed}=\lambda_m+W_m^{-1}\sum_I I^\chi_{I,m}.
\tag{119.9}
\]

这只是固定中心的完整源读出，尚不是 \(Y\) 的真实切口。

整个场使用原几何包中分别已付的

\[
A^\phi_{I,m}\ge\int_I|\phi_{1,m}|F\,dx,\quad
A^\chi_{I,m}\ge\int_I|\chi_{1,m}|F\,dx
\tag{119.10}
\]

以及 \(\sup_I|\phi_{P,m}|/V\)、\(\sup_I|\phi_{K,m}|/V\) 和对应 \(\chi\) 的界。将 (119.10) 乘本片完整 \(\mathcal N_m\) 的绝对上界，得到正的完整片贡献。

第一遍保存所有贡献并准确相加。第二遍对目标片维护已完成的 \(\phi\) 前缀和 \(\chi\) 后缀；后缀严格减去同一个已知 dyadic 片贡献。目标片内的两个部分积分均以各自完整正片贡献控制。因此对片上任意点，\(P\) 的归一响应由

\[
\frac{(1+m)e^{\sigma m}}{\inf|W_m|}
\left[\sup_I\frac{|\chi_{P,m}|}{V}
   (\text{前缀}+\text{本片}\phi\text{贡献})
+\sup_I\frac{|\phi_{P,m}|}{V}
   (\text{后缀去本片}+\text{本片}\chi\text{贡献})\right]
\tag{119.11}
\]

包围，\(K\) 同理。这里正列已包含物理 \(F^{-1}\)；源积分仅含一次 \(F\)，Wronskian 仅除一次，未额外引入 \(r_x\)。全部 10878 个目标片消费后，所有准确后缀同时归零。

实际全片/全模结果为

\[
\boxed{\|\mathcal G\Pi_{46}\mathcal N(L_R)\|_X
\le D_L=1.3059811148108280145\ldots\times10^{-13}.}
\tag{119.12}
\]

例如 \(m=4\) 的 \(K\) 响应界约 \(1.30455\times10^{-13}\)，而 \(m=6\) 的 \(K\) 响应界约 \(8.03089\times10^{-19}\)。所有 46 行都保存在完整主包中，没有用这两行替代整个和。

## 4. 对原真实解的准确后验结论

R105 已在同一 R100 完整单位参数域给出真实低 46 投影解，且其所在的绝对 9 球具有完整源收缩界

\[
\gamma=0.0024794106182418753\ldots<1/400.
\tag{119.13}
\]

原完整非线性内头提升（包括真实 far 一次）满足

\[
\|\mathcal B\beta(a)\|_X\le B
=3.6800149224305034\ldots\times10^{-17}.
\tag{119.14}
\]

使用原整个绝对 9 球上的同一导数界，而非本次中心 Jacobian，在 \(Y\) 与 \(L_R\) 的连接线段上由 (119.2) 得

\[
\|Y-L_R\|_X\le B+D_L+\gamma\|Y-L_R\|_X.
\tag{119.15}
\]

实际准确有理数消费给

\[
\boxed{\|Y-L_R\|_X\le\frac{B+D_L}{1-\gamma}
=1.3095961428853496\ldots\times10^{-13}
<1.31\times10^{-13}.}
\tag{119.16}
\]

也可直接选 \(\rho=3/(2\cdot10^{13})\)：\(\|L_R\|_X+\rho<8<9\)，且 \(D_L+B+\gamma\rho<\rho\)。故此小球自映并收缩。它的解与原 R105 解由绝对 9 球内的唯一性相同，没有另造一条未经识别的投影分支。

`root_full_linear_recentring_gates.py` 实际执行全部 17 项 Fraction 门，均为真。正文显示小数只作阅读；比较使用主包中的准确 dyadic 和有理数。

## 5. 实际证据和没有支付的部分

完整源/响应入口 SHA256：

```text
987435e9cb25e8bb294623920a6d891f7c346d7762bd06055c1dc184e1950d3f
```

原完整 Laurent 公式来自已固定的 `root_outer_actual_finite_dn4_v2.py`，SHA256 `3eeb508e6a865ca3549bd25f2824a580a758a9f55a13a4b15bf016cc917a6bc0`。新入口正式退出 0，实际 wall 272.086031 秒，峰 50912 KiB；无新 ODE 或 Node 求解。全部原材料、几何和新源块的完整哈希链保留。

完整主包 `2026-11-13-root-full-linear-source-r1-summary.json` 的 SHA256 为

```text
58ae9b5d9332ce09530d2380b00348eb50efa3693a27294ecf185d9ea6f175db
```

350 件新派生源块共 103239918 字节可由保存的源码、准确参数、原输入和 resource argv 复现；按仓库规则保存完整 manifest，不把可再生大工作文件重复加入 Git。当前工作副本全部保留供真正的新中心 Jacobian 和逐模消费者读取。

准确后验门主包 `2026-11-13-root-full-linear-recentring-r1.json` 的 SHA256 为

```text
a04967ff99f5c119636227b7e84c9be02a0fb80cec9d07ae7c8af69e03b89362
```

此前对旧混合中心的实际逐模消费者正式退出 0，但切口上界约 514373，远未通过。其完整结果、首次因 rebase 短暂移走输入而 exit1 的资源记录均保留在 `2026-11-13-root-true-modal-failed-cut-manifest.json`。它没有数学反例意义，也没有被改名为成功。新的中心消除了已知 \(L_R-Z_0\) 被计入未知修正的损失；后续仍须消费新的完整导数、实际 \(Y-L_R\) 源变化、R100 真内头与全部切口。R116 的旧中心数值矩阵不能直接当作新中心的矩阵。

参考：[R87](R87-complete-low46-physical-trace-flow.md)、[R100](R100-hybrid46-parameter-chart-and-source-transfer.md)、[R105](R105-actual-signed46-residual-and-small-projected-ball.md)、[R109](R109-complete-source-polynomial-and-frequency-jacobian.md)、[R116](R116-actual-low46-centre-jacobian-and-quadratic-remainder.md)。
