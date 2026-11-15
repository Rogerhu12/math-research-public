# s=2 完整第三连接：复用原 592 单位及已成第二余量的单 RHS 接口

日期：2026-11-15  
作者：AI（ChatGPT；Astra-ISP-789f / literature_audit）

## 输入是已成完整第二连接

本入口必须读取实际完整高块 $5100\times3762$ 的有理秩 $3760$ 及两条真实高核证明；不接受先前仅 normal≤3 的条件分支作为完整第二连接。现在完整第一、第二首项维数分别为 $15,14$，后者与原投影第二首项空间相同。

所有完整二阶 cochain 的三个系数都支撑于 pure/one-normal：同头差等于 $t$ 乘一个完整第一阶 jet。原投影第三页提供十三个真实首项，所以仅剩一个新的第三 RHS。

完整第三 incoming 必须包括全部 $A_1^T\Lambda$ 以及全部十五个第二强迫项。本入口用已成十四条投影二阶 cochain 和实际首项框架核验：

$$
\operatorname{im}R_2\subseteq\operatorname{im}M+\mathbb Qr_2,
$$

其中 $M$ 就是父任务的 $1088\times594$、秩 $592$ 常矩阵，$r_2$ 为已付唯一第二缺口。不能仅沿用七个第一 incoming 列。

## 只新增一个单位求解

父任务已经保存原主列 $P$、原单位行 $I$、$U=M[I,P]$、完整齐次核、真实原解 $X_2$ 及全部行余量

$$
UX_2=-r_2[I],\qquad S_2=r_2+M[:,P]X_2\ne0.
$$

新任务只求

$$
UX_3=-r_3[I],\qquad S_3=r_3+M[:,P]X_3.
$$

实际检查完整 $1088\times2$ 矩阵 $[S_2,S_3]$：

- 若秩为二，唯一第三 RHS 不相容，完整第三首项为十三维，$\beta_{3,\mathbb Q}=1$，原正谱为 $1^7,2,3$，总长为 $12$。与真实原投影的长 $12$ 比较，得到 $W/(L\cap W)=0$，九个原平方目标本身都局部入像。
- 若秩为一，写 $S_3=qS_2$，则 $X_3-qX_2$ 与真实 incoming $-qr_2$ 给出原完整第三延拓。完整第三首项为十四维，$\beta_{3,\mathbb Q}=0$；余谱只可能 $1^7,2,4$ 或 $1^7,2,5$。继续下一页，不将这个前缀当作完整成员性结论。

所有相容 cochain 都在原 $6188$ 来源及四层 Taylor 系数上乘回。完整原投影第三十三列由新的小 $1088\times186$ 原矩阵恢复并全原乘回；没有重做旧 $592$ 或 $583$ 常矩阵 RREF，也没有重求旧 RHS。

## 最终源码

建议路径：

notes/2026-11-15-r150-two-one-complete-rational-third-connection-789f.py

- 最终 blob：fb78922bc561bf2b402530fb6eeba79b40fa1057
- 21509 字节
- SHA256：f76ada7fd120bf2dbe6320d6341a8543d0cc54f92cf66d9625646efecf008eab

早期 blob 420fa407 不是最终版本。最终版本不假定第二阶代表的一次系数纯切向部分为零；所有真实原系数按父来源原样保留。

## CLI

建议 step：two-one-complete-rational-third-connection

同一共享时钟 180 秒 / 4096 MiB，outer 210 秒。没有 native 新依赖；使用现有实际成功的 python-flint Dixon 解一个 RHS。

~~~text
python {scripts}/2026-11-15-r150-two-one-complete-rational-third-connection-789f.py \
  --paid-probe {scripts}/2026-11-15-r150-two-directed-original-left-two-jet-witness-789f.py \
  --generator {scripts}/2026-11-15-r150-original-transverse-first-connection-789f.py \
  --jet-actions {scripts}/2026-11-15-r150-original-comoving-jet-actions-through-seventeen-789f.py \
  --two-four-generator {scripts}/2026-11-15-r150-original-comoving-two-coefficients-through-four-789f.py \
  --unit-schur-helper {scripts}/2026-11-15-r150-exact-actual-rhs-unit-schur-kernel-789f.py \
  --paid-second-receipt {scripts}/43740928483-two-one-true-rational-second-connection.json \
  --paid-high-receipt {scripts}/43740928483-two-complete-normal345-high-field17.json \
  --paid-checkpoint-dir {work}/two-one-true-q-second \
  --checkpoint-dir {work}/two-one-complete-q-third \
  --out {work}/two-one-complete-q-third-receipt.json \
  --remaining-seconds 180 \
  --memory-mib 4096
~~~

精确 pin：

- 第二回执：950aecf40605fbd3156c223d7e18d4ee1821940386872f59d88cc24f756ed1a2
- 完整高块回执：1582aa530b7439636798e33cf447ce46c3e85b352ab47b1e236cccc56525584a
- 原参数 through-four 系数模块：7b0ec2814a716e236d2dce048d0c8b1b6cea6bca8400e54d846b8e403aa1b7b9
- paid-probe：8f55c5b5f0db2a7dd9b0b042e00cd506fd6e38698b9dc264a602e3dc8ccb510b
- generator：2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186
- actions17：2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332
- 原单位 helper：36356983e71ee1e67677da1a7a5f7aebf2987db282a5447a741b6a6af93084d5

父 binding：
3de42bed91acf562cce951f7c79f9e4f871cbd31ec82e7430d03bb97198f970f。

实际高块 binding：
28bddf30e73c27eb623837d9569c9b43db83bd93f54d6ce84eedef0f24d0e862。

## 缓存与范围

父 cache 只读，所有所读 phase 的 verified、原文件 SHA、逻辑矩阵 hash、长度与实际回执逐一比较。子 cache 新 binding 包含全部来源及两个 actual。原 primitive 单位仅复制已核的常数行比例，绝不把旧 RHS 元数据用于新 RHS。

子任务保留全部新实际 cochain、首项映射、两个 Schur 列及原恢复比例，仅在当前临时 job。未完成时不报连接秩，已保存新 RHS 候选可按原 helper 续验。小回执保留来源链和哈希，不上传大数组。

若进入第四、第五页，必须先检查新三阶 cochain 的实际高部及下一强迫项；不能在未核新高 forcing 的情况下宣称以后永远只用相同低单位。
