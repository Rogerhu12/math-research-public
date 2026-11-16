# 原六均值的三十条首层乘法来源与完整权七秩 312

作者：Astra-ISP-789f / normal_annihilator，与 /root。AI-assisted GPT-6 Astra Pro。

## 1. 本页已经完成的结论

在原固定合法系数映射 $E\to k=\mathbb F_{127}$、$d\mapsto100$ 下，令

$$B=k[y_0,\ldots,y_5,w_0,\ldots,w_5].$$

全部十二参数均保留。由已付原十生成元模型的五个参数乘法矩阵 $N_i$ 和六条均值关系 $Y_j$，定义

$$V_{ij}=N_iY_j\quad(0\le i<5,\ 0\le j<6).$$

本次实际完整计算证明：

1. 三十条 $V_{ij}$ 各有逐原十八生成元乘回验证的多项式来源；
2. 六均值乘全部权二参数单项式的 162 列、已付二十条权六交换子乘全部六个 $y$ 的 120 列、三十条 $V_{ij}$，在完整 7754 行权七输出上构成秩 312 的矩阵；
3. 因而该 282 列前缀秩恰 282，三十新列在其 $k$ 线性商中独立，本次全部保留，没有删除列。

这是一项原来源与完整有限权空间结论。它不声称三十列相对已付五十列的整个 $B$ 子模独立，不声称该子模已对所有 $N_i$ 稳定，也不声称单位理想或特征零 Bell 自然幂成员性。

## 2. 同一原模型与来源公式

原十生成元向量为

$$m=(1,u_0,u_1,u_2,u_3,u_4,u_1u_4,u_2u_3,u_2u_4,u_3u_4)^{\mathsf T}.$$

原十八生成元列 $A$ 按五个 $u$ 梯度、六个 $w$ 梯度、六个 $y$ 梯度及 $b-1$ 排列。父模型具有完整身份

$$m^{\mathsf T}N_i=u_i m^{\mathsf T}-A^{\mathsf T}S_i,
\qquad m^{\mathsf T}Y_j=A^{\mathsf T}\sigma_j.$$

所以不需求新的大矩阵来源，直接取

$$\tau_{ij}=u_i\sigma_j-S_iY_j$$

便有

$$m^{\mathsf T}V_{ij}=A^{\mathsf T}\tau_{ij}.$$

本程序实际重新核了五十个原乘法列身份、二十六条所用父种子的完整原十八来源、三十个新来源及三十个最终表达式的全部十参数坐标和十八原源乘回。原十七梯度与此坐标系之间的完整 Jacobian 运输仍由同一父模型及其精确文件身份固定。

父模型及原五十列子模的来源范围见 [原参数种子五十列与完整有限域模等价](R150-appendix-original-parameter-seeds-fifty-and-complete-field-module-equivalence.md)。本页沿用其全部原参数与原生成元，没有另取参数点。

## 3. 全部权七原行与原列

取参数权 $\operatorname{wt}(y)=1$、$\operatorname{wt}(w)=2$，模生成元权 $(0,2^5,4^4)$。记 $B_d$ 为所有十二参数权 $d$ 单项式，则

$$|B_1|=6,\quad |B_2|=27,\quad |B_3|=92,
\quad |B_5|=714,\quad |B_7|=3816.$$

故完整输出字典的行数为

$$3816+5\cdot714+4\cdot92=7754.$$

完整原输入字典依次为

$$\{qY_j:q\in B_2,\ 0\le j<6\},$$

$$\{y_aC_\ell:0\le a<6,\ C_\ell\text{ 为已付二十条保留权六交换子}\},$$

$$\{N_iY_j:0\le i<5,\ 0\le j<6\}.$$

列数恰 $6\cdot27+20\cdot6+30=312$。每个原列标签、参数指数、完整输出指数及所有非零系数均实际保留；任何非零项不在声明字典中即失败。

已付七位面 F127 算术 native 的源码和头文件逐字复用。它先通过 244990 项域运算检查和 25 项独立普通标量小矩阵乘回，再处理全部 312 原输入行。在此次实际运行中发生 32724 次完整主元消去，取得 312 个归一化原单位行，没有目标依赖式。全部输入列已经处理，不是提前截止下界。

因为输入总数就是 312，所以实际秩 312 已是精确秩。任意前缀列子集同样独立，特别是原 282 列前缀秩 282，三十新列在其常数线性商中的维数为 30。

## 4. 对后继原来源搜索的准确用途

设 $L_0\subset B^{10}$ 为已付五十原列生成的参数子模。当前三十条新列都具有完整原来源，故可以组成

$$L_1=L_0+\sum_{i,j}B\,N_iY_j.$$

本次筛选将三十条全部保留，因此没有额外压缩。全部 282 前缀均属于 $L_0$，但本页没有把它们称作 $L_0$ 的完整权七部分；尤其原 Bell 列未参加该齐次前缀。因此本页不由上述秩断言 $L_1\ne L_0$。

若后继在 $L_1$ 内真实构造 $e_0$ 的参数来源，仍须把该来源经三十个 $\tau_{ij}$ 和五十个旧原来源逐层回填，核全部十坐标、原十八生成元及原十七梯度加 Bell 的完整乘回。反之，某次候选搜索未找到 $e_0$，不能据此称原理想非成员。所有特征零来源必须另在 $E$ 上完成实际乘回。

## 5. 本次实际身份

本地独立执行采用 Python 3.12.14、python-flint 0.9.0，严格复用原父物理文件 SHA。命令、全部依赖源的 path/blob/bytes/SHA 及 180 秒、768 MiB、外层 240 秒预算记录在：

- `notes/2026-11-16-r150-original-mean-first-frontier127-inputs-789f.json`；
- `notes/2026-11-16-r150-original-mean-first-frontier127-interface-789f.md`；
- `notes/r150-original-parameter-module-execution-789f/local-20261116-original-mean-first-frontier127-180.json`。

主源为 `notes/2026-11-16-r150-original-mean-first-frontier127-789f.py`，Git blob `049028bbcfa486e8335d589c203d7cf682c4d7ac`，18470 bytes，SHA-256：

~~~text
810904a2c797b08493ed377c069abd75018e0a0df8035cb700baad80616bea1e
~~~

实际 exit 0，状态 `completed`。总 elapsed `17.096617878007237` 秒包含编译、构造、完整核验和封存；native 数学段为 `0.200218` 秒。父进程峰值 106044 KiB，子进程峰值 157672 KiB。

主 binding：

~~~text
9502b11bf94390e8833cdc236a1ad85746d9823f9f4fe1e62de60f1932434bfd
~~~

| 临时对象 | Bytes | SHA-256 |
|---|---:|---|
| 完整 raw 回执 | 25766 | `20405495e04e812ddd06366e1edd300f4cf7d612ccc959eeadb836a9323594ea` |
| 完整 manifest | 25958 | `2b2011f80201661ab7b9680aeb86f8f11414244b4adbf21a6fb2728babfa72c9` |
| 全部原行输入 | 2419340 | `23430d41a72391d2f7cd36efc2e7517cdd05187601ec654fec51d62c9224294d` |
| 完整原字典 | 245111 | `3463ec53d58d0d49d5f3298b3364d411e2a1a98beca49f63561df5aaf73c45da` |
| 完整 native 状态 | 2212820 | `c5553497e614338fc5a811ad5bce78571d1d835e32f269435f756e822e2e35df` |
| 完整 native 结果 | 2612 | `3996c60c05f2fadb339c7d4f9d411c0e75fb82ed103d875077fa93f207d7d020` |
| 最终来源证书 gzip | 1497 | `f9c26d66aead9520f4603911832b44739464a69794c8c4598b9dd31ecdedfe38` |

最终证书解压逻辑 bytes 为 8958，SHA-256 为 `0ca00c8204cbf1fabf2f022ffd8bd4d6a4fca4e484e66a926832d083cc3d0698`。全部 61 个完成阶段具有完整物理和逻辑身份。所有数组及原 raw 仅在临时目录；仓库不保存可重算数学数组。

## 6. 根代理的完整独立来源产品复核

根代理另用普通标量解码整个七位面检查点，再用 FLINT 的有限域矩阵乘法独立核验。它不调用 producer 的消元函数或位面运算。令全部原 312 列转置所得矩阵为 $X\in k^{312\times7754}$，从完整检查点解出来源系数 $Q\in k^{312\times312}$ 及归一化行 $R$。实际检查

$$QX=R$$

的全部 2,419,248 个坐标，并核每行首个非零坐标恰为 1、312 个主元互异、全部原来源编号恰为 0 至 311、没有未来来源系数或非零填充位。因此原有限矩阵满列秩的见证已独立完整乘回。全部 61 个源阶段的物理和逻辑 SHA、全部 native 文件身份也核过。

独立源为 [2026-11-16-r150-original-mean-first-frontier-full-product-audit-789f.py](../notes/2026-11-16-r150-original-mean-first-frontier-full-product-audit-789f.py)，5174 bytes，SHA-256：

~~~text
4f4fad0c7b67b8c89a11a2068a7258cbb8a3a778da504943e364f717c3c6cf47
~~~

实际 session 29733，exit 0，15.648538335997728 秒，峰值 115092 KiB。完整临时复核 raw 为 885 bytes，SHA-256：

~~~text
352df46ca37fa38bfa8ed5e3186ac2c784570a10b005a5bf0eea046b7c2f251e
~~~

执行身份见 [root 全产品复核身份](../notes/r150-original-parameter-module-execution-789f/local-20261116-original-mean-first-frontier-root-full-product-audit.json)。预检曾因 native 文件实际位于 complete-weight7 子目录而报 FileNotFoundError；修复路径基准后才得到上述实际完整成功，没有将预检算作数学失败或预算进度。复核过程不写任何新数学数组。它不扩大第 4 节的有限权范围。
