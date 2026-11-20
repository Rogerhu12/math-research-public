# 严格同像径向重参数化：2b143 的一次真实复合试验

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / recover_evidence。

**结论：这22维切向子空间只消去约0.504%的原加权 SSE，完整有限 maxGram 略升；不作为主线新父。** 数学复合严格保持父像集合，有限目标始终使用原 $a(s)$；没有把 a 一起复合，没有将高次复合场假称原 quintic。

## 准确机制与线性化

设父场为 F，令 $\sigma(s)=s+\xi(s)$ 严格递增，在两端及 lift 断点邻域恒等。准确新场

$$\widetilde F(s,\phi)=F(\sigma(s),\phi)$$

的像集合与父相同。因为 $\sigma$ 是 $[0,S]$ 上保持端点的单调双射，映射的像包含关系双向成立；$\sigma'>0$ 和 $C^2$ 正则性给 $C^2$ 逆。闭合、嵌入、reach、直径及以空间点定义的支持／距离性质都属于同一像，不需重新扫描来发现不同的几何值。这里只继承同一父实际具有的性质，不能借用其他父的数值证书。

记父的三个未归一化 Gram 分量为

$$E=F_s\cdot F_s,\quad B=F_s\cdot F_\phi,\quad G=F_\phi\cdot F_\phi.$$

准确有

$$
\widetilde E=(\sigma')^2E\circ\sigma,\quad
\widetilde B=\sigma'B\circ\sigma,\quad
\widetilde G=G\circ\sigma. \tag{1}
$$

在 $\sigma=s+t\xi$、t=0 处，

$$
\delta E=E_s\xi+2E\xi',\quad
\delta B=B_s\xi+B\xi',\quad
\delta G=G_s\xi. \tag{2}
$$

其中

$$
E_s=2F_s\cdot F_{ss},\quad
B_s=F_{ss}\cdot F_\phi+F_s\cdot F_{s\phi},\quad
G_s=2F_\phi\cdot F_{s\phi}.
$$

所以既有六 jet 足够。原目标 $g=ds^2+a(s)^2d\theta^2$、$\rho=\Theta_\phi$ 不变；相对残差三项的切向列准确为

$$
\delta r=
\left(E_s,{B_s\over a\rho},{G_s\over a^2\rho^2}\right)\xi+
\left(2E,{B\over a\rho},0\right)\xi'. \tag{3}
$$

这不是把目标 a 改成 $a\circ\sigma$。基于 (3) 对全部原节点／中点及六 Gauss 行、完整角重数与 Frobenius 权 $(1,2,1)$ 累积小正规系统。每个径向 stage 的五个角收缩量足以构成全部 $22\times22$ 正规矩阵和梯度，无需存储一份完整大 Jacobian。

## C² 参数与严格单调性

采用22个紧支撑基

$$
\psi_j(s)=
\begin{cases}
(1-((s-c_j)/w_j)^2)^3,&|s-c_j|<w_j,\\
0,&|s-c_j|\ge w_j,
\end{cases}
\qquad \xi=\sum_jb_j\psi_j. \tag{4}
$$

边界三阶零保证 $\psi,\psi',\psi''$ 与零片相接，故整体 $C^2$。全部中心／宽度及本次拟合系数按实际 binary64 解释为准确有理参数。

支持最左端准确为1，最右端为

$$ {2610961883968045\over1125899906842624}.$$

此支持完全位于准确 $S-w$ 左侧；利用已刊 S 下盒，断点到支持右端的准确距离下界为

$$
{9877873864550011601238759544531\over4294967296000000000000000000000000}>0.00229987.
$$

因此 core、整个活动 lift 区及终端都在恒等邻域内。

将所有 $c_j\pm w_j$ 排序后得到42个非空内部 piece。在每个 piece 上，$\sigma'$ 是准确五次式，因为

$$
\psi'_j={-6x+12x^3-6x^5\over w_j},\qquad x=(s-c_j)/w_j.
$$

源码用 Fraction 将其转换为该 piece 的 Bernstein 五次系数；各系数的最小值是整片下界，外部导数为1。本次所得准确有理最小值严格大于0.99317，最大值严格小于1.007552。报告保存完整有理分子／分母；这是真正单调性证明，未用采样最小导数替代它。

于是 (4) 定义的实际全步 map 是严格单调的，像集合保持结论已经成立。此证明不把普通浮点 Gram 读数升级为连续 metric 证书。

## 同一父的真实复合读出

固定父：

work/geometry_path/curvature-qp-protected-992-twelve-step.npz

SHA-256：

2b143b5fb1f68c6bb9fe46ccc748755e125629786e072d8eb42e4903e4e4d453。

原 same-g Gauss carrier SHA 是 71fdec7b9b471cc7e202a859e6907de256f8117f252798baaad794ccab918112；全部7377径向行、完整 N2048 角重数、原半 Simpson／半 Gauss 径向权都保留。没有加入额外几何扫描。

22列全部保留；归一化正规矩阵最小／最大特征值约 .0399801、2.0460431，条件数约51.18。纯线性最小二乘预测加权 SSE 从 .2898137755349494 降至 .2883579151549931。准确复合的第一个全步通过单调性并降低真实有限加权目标，不需要进一步回溯。

| 同一有限目标 | 父 | 真复合全步 |
|---|---:|---:|
| 原加权 SSE | 0.2898137755349494 | 0.28835308865374576 |
| 加权均方 SSE | 5.967639701434925e−5 | 5.9375622732397116e−5 |
| 全行未加径向权 SSE | 669.9280674677264 | 669.0476852989801 |
| 全行 maxGram | 0.04620001982850197 | 0.046237571058598714 |
| 旧节点／中点 maxGram | 0.04620001982850197 | 0.04088788782093489 |
| 新六 Gauss maxGram | 0.04609215587280757 | 0.046237571058598714 |

最大观测位移 .00011416066301269456；最坏有限 maxGram 从旧 stage1787、s2.3112662789819365 移到新增 stage7206、s2.313660486716928；角均为 $\pi/2$。后者实际查询父位置 s2.3136519746683564。

加权 SSE 下降0.5040087824%，而全 maxGram 上升0.0812796839%。如果只保旧行，就会错误地认为最大误差明显改善；本次全部新行仍参与拟合和读出。

报告另有逐 stage 独立 shift／stretch 两列松弛的数值拟合量 .0603822。该松弛忽略 $\xi$ 与 $\xi'$ 的相容性，且使用普通浮点伪逆／截秩；它只是数值线性诊断，不是全局可达减少量或严格的不可改进下界。不能据此声称已排除所有径向重参数化。

## 准确模型扩展与重采样的区别

若将来更丰富切向方向显示足够收益，可以把父 q 的完整三 jet 与少量单调 $\sigma$ 参数一起作为模型变量，保持准确复合求值。支持内 $\sigma$ 为六次式，父 q 为五次式，故在原 knot 的准确逆像及 bump 分界之间，复合一般可达30次，已经不是原 quintic。原节点的逆像唯一，由严格单调性保证；可用有界根隔离维护准确 piece。

其六 jet 准确为

$$
\widetilde F_s=\sigma'F_s\circ\sigma,\quad
\widetilde F_{ss}=(\sigma')^2F_{ss}\circ\sigma+\sigma''F_s\circ\sigma,\quad
\widetilde F_{s\phi}=\sigma'F_{s\phi}\circ\sigma,
$$

角导数直接与 $\sigma$ 复合。这个扩展仍使用原 $a(s)$，全部原目标行可以原样保留；几何按同像继承。

另一种方案是在若干新节点取上述三 jet 后重新作 quintic Hermite。这是一个新场，通常与准确复合不同，不能再自动继承同像、reach 或曲率性质；必须单独支付插值误差或继续原完整模型求解。本次没有执行此重采样，也没有发布一个假称原空间解的 NPZ。

本次弱收益不足以替换正在进行的主线。该结论只描述上述22维试验，不证明所有切向机制无用。

## 完整源码与实际身份

完整源：[fullclosed_radial_reparameterization_trial.py](../scripts/resume_20261120/fullclosed_radial_reparameterization_trial.py)，16,286 B，SHA-256：

fec3425b9c10b44f1d9b5d210a9f4ca8f182ff21edf1dc5c9d51bb418d12530c。

它消费原 dense、R653 batch、R655 Gauss observation 模块，复用原真实 Hermite／解析 lift 求值，不修改这些源。参数中心／宽度在源码中，实际系数、完整 Fraction 单调界、基准和 trial 全在 scratch 报告：

work/recover_evidence/radial-reparameterization-2b143-first.json

SHA-256：

f063b72d76f3d84c3dc1606b1f2a5560f678fe08297f595b2a0e080718100b2b。

session50166 自然返回0，总耗时2.19秒。可重生 raw 不入库。实际命令为：

```bash
python -u math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_radial_reparameterization_trial.py \
  --bundle work/geometry_path/curvature-qp-protected-992-twelve-step.npz \
  --carrier work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz \
  --node-report work/fullclosed_solver/data/fullclosed-hold-warm.json \
  --operator math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py \
  --batch-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_batched_closed_gram.py \
  --observed-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/gauss_observed_closed_gram.py \
  --out work/recover_evidence/radial-reparameterization-2b143-first.json
```

公开CLI将原scratch执行源位置换为本仓库内的同字节源。cwd为含math-research-public与work的共同目录，单BLAS环境沿前序；父2b143/1240、carrier和节点报告依前序实际公开命令重建。原字段数组及完整逐点输出仅scratch，不以唯一文件路径替代完整配方。
