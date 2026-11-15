# 21 个第三头的原四层回填：复用旧 166 列，仅解真实 144 小单位

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。  
日期：2026-11-15。

## 1. 当前实际入口

完整所选第三连接已经证明为 3，全部第三常头恰为 21 维，并已在旧 22 条真第二 cochain 中保存精确坐标 $Z$。本轮不重求这些头。

随后实际 v2 准备已经完成：

- 21 个原 $4354$ 维右端全保；
- 旧第一增广矩阵的 1736 个省略行上全部为零；
- 当前 $M_0$ 共有 1922 个空行，其中另外 186 行继续保留在完整原残差；
- prepared binding 为 3ac423ccd312ea0fa7084f70b9a2fb788a26822a62e9918998f17d6762fc371a。

新的 21 个旧 $1546$ 单位解也已真实完成，数学 26.761078060999353 秒，worker 26.314903170001344 秒。完整候选先保存，再核全部 $1546\cdot21=32466$ 原未缩放单位产品为零：

| 实际对象 | 字节 | SHA256 |
|---|---:|---|
| prepared 单位输入 | 5511912 | 675fea9cbc0be933f7c1dc742552184fd62ccdc21acd17efa9b5ba91de05b623 |
| 完整原 21 右端 | 4617848 | 22d41ddbd72836d013f0855cf094f243ae5bc63a07f9006b9603031383794598 |
| 21 个完整有理解 | 9850907 | 92f802330ac3c61fa30dc31b03b43ca4dfd534e4539f5d1ffde2a344a2829366 |
| unit worker 回执 | 2131 | f65f843bef9856075220b87c1870edbee50cdf8f5bbbad09564db1c8fbb0303d |

这些只付单位行，尚未付完整 $\lambda_3$。本消费者承担全部原残差、低层补偿、真实来源回填和四层原乘回。

## 2. 固定源码与预算

源码：

- notes/2026-11-15-r150-third21-normal-four-original-consumer-789f.py；
- blob 9c84f8d93fa07550e97bba888c149462aad130b9；
- 32637 B；
- SHA256 89a1e354928c70a9ff9aac28e1935d78739ea760ce39bb8b58dc2f7cf378c854。

本地环境不可用，本文不虚报本地 AST 或本轮数学结果；首次实际运行时由 Python 解析源码。

~~~text
python -B {scripts}/2026-11-15-r150-third21-normal-four-original-consumer-789f.py
  --regauged-out {work}/selected-natural-second-left-regauged
  --normal4-out {work}/selected-natural-second-left-normal-four-complete130
  --first-out {work}/selected-natural-first-left-envelope
  --third-out {work}/same-source-koszul29-third-pairing
  --prepared-out {work}/third21-forcing-support-preparation-v2
  --unit-out {work}/third21-unit-solve
  --out {work}/third21-normal-four-original-consumer
  --seconds 300
  --memory-mib 4096
~~~

建议外墙 360 秒。共享数学时间 300 秒，每进程 4 GiB；源码允许不超过 600 秒、8 GiB 的后继显式预算，不改变数学 binding。没有编译和安装。

## 3. 旧 166 列与新 21 列的真实残差

记旧 $M_0$ 为原 $4354\times1546$ 纠偏矩阵。旧 36 列 $F_r$ 是 $[H_F,T]$；另外 130 列 $F_r$ 是完整 normal4 高核的真实原像 $M_4K_r$。所有对应的旧单位解已付
$$
M_{0,I_0}N_r+D_r(F_r)_{I_0}=0,
$$
并已保完整原残差
$$
S_r=M_0N_r+D_rF_r\in\mathbb Z^{4354}.
$$
完整 $S=[S_1,\ldots,S_{166}]$ 的已付 Q 秩是 $144$。旧 36 和新 130 的全部解及来源均复用，不重新求它们。

对新 21 个右端
$$
q_j=R_3Z_j/g_j
$$
及刚完成的真实单位解 $(n_j,d_j)$，先构造全部原行
$$
v_j=M_0n_j+d_jq_j.
\tag{3.1}
$$
每个 $v_j$ 都保存完整 4354 坐标，并重新核旧单位行确实为零。1736 个旧省略行之外的全部行，包括额外 186 个 $M_0$ 空行，都保留。

## 4. 真 144 小单位、同步尺度与全行 Schur

使用已付原 $166$ 列 RREF 的 144 个主元列 $S_{p_r}$。为了避免大公因子污染精确求解，分别取列内容
$$
c_r=\gcd(S_{p_r}),\qquad t_j=\gcd(v_j),
$$
零目标列取内容 1，定义
$$
B_r=S_{p_r}/c_r,\qquad V_j=v_j/t_j.
$$
再按 $B$ 每一原行的 gcd 选真实小单位行。实际选行最多使用固定两个算法素数 $31,65521$，并核所选 $144\times144$ 子式模该素数非零。这个步骤只选择一个已知 Q 秩 144 矩阵的真实单位子式，**不作新的原全矩阵素数秩结论**。

矩阵与右端在相同原行上同除行 gcd。右端保有理数，不要求其被 gcd 整除。精确求解
$$
U X=-V_{I_U}.
$$
完整 $144\times21$ 解先以正列分母 $D_j$ 和整数分子 $N_{\cdot j}$ 保存，随后才核原单位产品和全部原行残差
$$
R_j=D_jV_j+\sum_r B_rN_{rj}.
\tag{4.1}
$$
全部 4354 行保留。若所有 $R_j=0$，21 个头全部在该 normal4 纠偏空间可成；否则求 (4.1) 的完整 Q 核，并对每个核组合核全部 4354 原残差为零。

设整数 $\kappa$ 是保存的 (4.1) 原坐标核向量。真正返回未缩原残差的系数是
$$
\beta_j=\frac{D_j\kappa_j}{t_j},
\qquad
\gamma_{p_r}=\frac{\sum_jN_{rj}\kappa_j}{c_r},
\qquad
\gamma_r=0\quad(r\notin\{p_1,\ldots,p_{144}\}).
\tag{4.2}
$$
故严格有
$$
\sum_j\beta_jv_j+\sum_r\gamma_rS_r=0.
\tag{4.3}
$$
所有列 gcd 和行 gcd 都保存。代码不把规范化矩阵的核直接当原来源系数。

## 5. 原四层来源的回填公式

展开 (4.3)：
$$
M_0\left(\sum_j\beta_jn_j+\sum_r\gamma_rN_r\right)
+\sum_j\beta_jd_jq_j+\sum_r\gamma_rD_rF_r=0.
\tag{5.1}
$$
因此基础三个 cochain 同时取
$$
(L_0,L_1,L_2)\sum_j\frac{\beta_jd_jZ_j}{g_j}.
$$
再令
$$
a=\bigl(D_r\gamma_r\bigr)_{\text{三列 }H_F},
\qquad
y=\bigl(D_r\gamma_r\bigr)_{\text{三十三列 }T},
$$
$$
x_3=\sum_j\beta_jn_j+\sum_r\gamma_rN_r,
\qquad
\eta_4=\sum_{\text{130 新列 }r}\gamma_rD_rK_r.
$$
最后真实来源为
$$
\lambda_0=L_0\sum_j\frac{\beta_jd_jZ_j}{g_j},
$$
$$
\lambda_1=L_1\sum_j\frac{\beta_jd_jZ_j}{g_j}+\Lambda Cy,
$$
$$
\lambda_2=L_2\sum_j\frac{\beta_jd_jZ_j}{g_j}
+\Lambda Fa+E_{\rm old}Xy,
$$
$$
\lambda_3=E_{\rm new}x_3+E_4\eta_4.
\tag{5.2}
$$

旧的 22 个 primitive cochain 自身还约去过各自的共同 gcd；代码再次返回原保存的旧第二变量时，明确除去这一旧因子。新 $g_j$、旧 cochain gcd、span 的 $c_r,t_j$ 是四组不同尺度，不混用。

(5.2) 先作为同一有理参数向量组合，再统一清分母、约去所有参数的共同 gcd，得到整数 cochain。随后才在同一全部原 $4354$ 来源上核
$$
B_0^T\lambda_0=0,
$$
$$
B_0^T\lambda_1+B_1^T\lambda_0=0,
$$
$$
B_0^T\lambda_2+B_1^T\lambda_1+B_2^T\lambda_0=0,
$$
$$
B_0^T\lambda_3+B_1^T\lambda_2+B_2^T\lambda_1+B_3^T\lambda_0=0.
$$
每列 $4\cdot4354=17416$ 个原整数产品必须全零。候选完整四层原 $4367$ 坐标先保存，再记录逐列完整验证。最后在真实 33 个第一头坐标中再核所得头独立。

## 6. 完成范围与下一页边界

如果实际产出 $h=21$ 个独立真头，则完整第三头空间的显式四层来源全部完成。否则仅完成该 normal4 支撑所允许的实际 $h$ 维子空间；不得否定已经证明的完整 21 维全局第三头存在性。

主回执：
third21-normal-four-original-consumer-receipt.json。

完成 outcomes：

- complete-original-third-cochains-normal-four；
- restricted-normal-four-third-cochains-only。

关键字段：

- actualExplicitThirdHeadDimension；
- all21CompleteThirdHeadsExplicit；
- allOriginalFourLayerProductsZero；
- originalFourLayerProductCoordinates = $17416h$；
- allActualHeadCoordinatesIndependent；
- correctionNormalDegreeAtMost = 4；
- old36And130UnitSolutionsRecomputed = false；
- completeFourthIncomingImageComputed = false；
- knownFourthIncomingImageDimension = 13；
- completeFourthIncomingImageDimension = 15；
- remainingFourthIncomingImageDimension = 2。

本轮不计算第四 forcing，也不把 13 维已知低页像冒充完整 15 维低页像。若以后完整 21 个真第三 cochain 在 $E/W_{13}$ 中的第四像秩为 $r$，已付前三层 Q/F31 秩相同允许下界 3，故完整第四连接只可先报
$$
\max(3,r-2)\le\operatorname{rank}\beta_4\le r.
$$
$r=3$ 才在这一路径上闭合为 3。

## 7. 恢复与存储

两个实际阶段为 residual-span 和 original-products：

- 每个新完整原残差独立原子保存；
- 144 个真实原单位行及所有尺度保存；
- 完整 144×21 候选先保存，再做全行 Schur；
- 完整目标核和实际头组合保存；
- 每个原四层候选先保存，再核每个原产品；
- 完成列带原 candidate SHA 的独立验证回执；
- 同 binding 续接复用已成数组与已核列。

暂时没有返回完整解的原生 solve 不伪称可恢复其内部状态。所有已返回数组及完整检查点都保当前 job 临时目录，预算到时保存实际阶段。长期仅保存小源码、参数、run、SHA 和小回执，不上传大数据。
