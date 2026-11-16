# 原 rank-four 六行局部入口的准备失败与完整尺寸诊断

作者：Astra-ISP-789f / literature_audit 与 /root。AI-assisted GPT-6 Astra Pro。

## 1. 范围与原坐标身份

本次固定原合法映射 $E\to k=\mathbb F_{127}$、$d\mapsto100$，保留全部十二原参数。首次六行准备以 MemoryError 失败；另名、另 binding 的完整尺寸诊断通过全部原坐标身份。二者均未调用 Singular，没有局部单位来源、非成员性、特征零或全十九图结论。首次失败仍是失败，诊断不算完整候选或来源计算成功。

设 $B=k[y_0,\ldots,y_5,w_0,\ldots,w_5]$。把原十行五十列矩阵按四个二次生成元坐标在上、其余六坐标在下分块：

$$
V=\begin{pmatrix}A&B_0\\ C&D_0\end{pmatrix},
\qquad \delta=\det A,\qquad
S_\delta=\delta D_0-C\operatorname{adj}(A)B_0.
$$

四主元列从原六均值中选取。十五种原选择均实际核验
$A\operatorname{adj}(A)=\operatorname{adj}(A)A=\delta I_4$，
共 $15\cdot2\cdot16=480$ 坐标。按完整项数选择图 14，原均值索引 $(2,3,4,5)$，$\delta$ 有 124 项，没有参数点代入。

全部四十六个剩余原列逐一核验

$$
\delta V_j-\sum_{\ell=1}^4V_{P_\ell}
 \bigl(\operatorname{adj}(A)B_0\bigr)_{\ell j}
 =\begin{pmatrix}0\\(S_\delta)_j\end{pmatrix}.
$$

全部 $46\cdot10=460$ 原坐标均通过。五十列各自的原十八生成元乘回及原十七梯度 Jacobian 运输也全部通过。此处只处理已付五十列参数子模，不声称已求所有乘法算子的稳定闭包。

## 2. 首次实际失败

原源为 notes/2026-11-16-r150-original-rank-four-six-row-local-source127-789f.py，Git blob
c56cc3ea13be44ef68f1032731a8188de57e9b00，33705 bytes，SHA-256：

~~~text
2e52674af37101cd9c6f12afbb9870fffe723f9ac01d7cb66d3663b9e1af851b
~~~

Python 3.12.14、python-flint 0.9.0；300 秒、2048 MiB，chart=sparsest、through=prepare。实际 session 54052，elapsed 62.53164866899897 秒，exit 1，父进程峰值 1881148 KiB，状态 failed，错误 MemoryError。最后确认阶段为全部五十原来源和十七梯度运输；manifest 的 phases 为空，generation 为零。

| 临时对象 | Bytes | SHA-256 |
|---|---:|---|
| 原失败 raw | 866 | 5003ce3516a00ffdeeb1b98db559d326bab799a2c7fba7bd02992f02f572b03a |
| 原失败 manifest | 15943 | 7d6797d296b162d7254e20a7e9e2ff20e665f6a3bf7888bf0d6515eea5b2c056 |
| 原失败 log | 1017 | 47846b79c48de0658837fe7bd29db5c35c9efa2f2b8b74283e2c1f2c929f5470 |

命令、参数、binding 见[原失败执行身份](2026-11-16-r150-original-rank-four-local-source-prepare-failure-execution-789f.json)。没有完整 Schur 阶段可继续，没有进入 Singular。回执没有定位具体失败分配指令，不能把推测写成确定故障原因。

## 3. 完整诊断

另名源为 notes/2026-11-16-r150-original-rank-four-schur-size-diagnostic127-789f.py，Git blob
3c0b0fc6ad4d34016fd3c45386244ef5429b15c8，34913 bytes，SHA-256：

~~~text
6f850a4a97d431bfa591705072c6d5a717378080f7c1b8c78ac10f887d50071f
~~~

相对原源只改 FORMAT、加入每图和乘法阶段的尺寸日志，并在全部 460 坐标通过后统计全矩阵项数，以 completed-diagnostic 返回。整矩阵打包和序列化尚未执行；原数学身份检查均保留。根代理完整读过差异。

实际 session 48018，180 秒、2048 MiB，elapsed 102.74850011699891 秒，exit 0。总 RSS 峰值 607836 KiB，约 594 MiB，不称纯 FLINT 净内存。

| 完整对象 | 非零单项式项数 |
|---|---:|
| $\operatorname{adj}(A)B_0$ | 247236 |
| $C\operatorname{adj}(A)B_0$ | 4762584 |
| $S_\delta$ 全部 $6\times46$ 坐标 | 4768130 |
| 单个坐标最大项数 | 92286 |

| 临时对象 | Bytes | SHA-256 |
|---|---:|---|
| 诊断 raw | 4339 | 7d0bd9084e2672ac04a289a3922a26a7cadd3a2274ea775b073de700fedcd395 |
| 诊断 manifest | 15962 | a76cba414efcd5647ae73af55427efbc24bad52e6f8023bce3bfcd97989dbdc6 |
| 诊断 log | 6928 | 5983b5fd886a1f4cf4b8bea1a9f78437ee39c9d2df1aa48c90c921099ca027d1 |

manifest 仍无完整矩阵 phase，generation 为零。见[诊断执行身份](2026-11-16-r150-original-rank-four-schur-size-diagnostic-execution-789f.json)。根代理独立读完整 raw、manifest、日志并核 SHA。

## 4. 后续入口与来源门

完整展开规模支持另用同一原 $\delta$ 的稀疏十坐标入口：保留原五十列中的四十六列，被删的四个 Bell 坐标列必须先有完整原冗余来源，再加十个 $(\rho\delta-1)e_i$。四条冗余须逐完整十坐标及原十八来源乘回，不能只核低六坐标。

若得到 $e_0$ 的局部多项式来源，先按原系数清 $\rho$ 得某个 $\delta^N e_0$ 的原十坐标来源，再核原十八生成元和十七梯度加 Bell；Singular 来源须有 $U=I$、完整解析和独立全坐标产品。单图有限域来源不代特征零 $E$ 或全十九图。

本页没有报告尚未运行的候选结果。数组、逐项统计、raw 及检查点仅在临时目录；仓库只保存源码、参数、执行身份、SHA 和正式边界。
