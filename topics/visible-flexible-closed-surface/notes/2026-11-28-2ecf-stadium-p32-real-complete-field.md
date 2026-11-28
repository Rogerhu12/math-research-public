# p32 低坡度新 Γ95 至 R205 的完整材料场

用[四组真实 H65](2026-11-28-2ecf-stadium-full-gap-H65-slope-physical-inputs.md)中 $p=32,r=1/4,v=.012$ 的全 gap 中央和低曲率特例。实际 $A=1.41907007899\ldots$，$A-B=1.05292676173\ldots$。入口由其专属 Γ95 定义，原 cut 和固定帽不动，保留[p8 加长材料场](2026-11-28-2ecf-stadium-H65-real-complete-field.md)第三态的 14820 个物理位置系数作为固定空间背景。计算坐标 $x$ 到物理 $s$ 的钟沿用新 $S=1.001184050377338$ 的同一函数。完整位置中的旧增量以其真实物理坐标重新求导；未借用旧度量的误差或迭代次数。

新的前缀目标在新 ramp 内补入 $(F_0-1-vr/2)H_5$，其中 $F_0$ 是 Γ95 文件存储的准确正数，两端一二次导数为零，实际正 coast 从 $F_0$ 出发。精确数学定义令 $f_L=F_0+v\ell,\ell=.02$（二进主文件长），后缀的正五次函数通过其两端 $f_L,v,0$ 与 $.8,-1,0$ 两 jet，再乘以本次 G10 拟合的正指数半径。数值控制点是这些公式的浮点求值；输出 JSON 的旧键 `ell` 给出两个图界，真正的 coast 长度由同一新 master 读取。新冻结目标 SHA-256 是 `eb5d81299c2f6cb5e0e3a310b62444820f8625be40878bb22485ca9093ef4470`。位置在六个实际形变长度中经 G10 选择 .52，G11 未参与。源基线 G11 为 .32841791、18.14516446、held .61722476。固定 R205 的原独立角上 held 最小约 .76212。

各次试验都用原 G10 的 958 个径点、128 和 192 个整圈角、每点原 14 个物理行；独立 G11 的 668 个径点和 256 个实际错移角未进入训练。所有分辨率保留全 Cartesian、全部 Gram 交项、真实主曲率及实际 R219 空间约束。未在这些离散结果上推断全曲面 reach 或连续 metric。

| 阶段 | G10 metric | G10 曲率 | 两组原成本 | G11 metric | G11 曲率 | G11 held |
|---|---:|---:|---:|---:|---:|---:|
| 24 | 0.10257529 | 12.770148 | 0.027691192 | 0.10363428 | 12.773013 | 0.61930148 |
| 60 | 0.098935733 | 12.018201 | 0.029750719 | 0.10558779 | 12.14263 | 0.61836226 |
| 115 | 0.097082778 | 11.850668 | 0.029549287 | 0.10670755 | 12.229721 | 0.61806748 |

三段每段 80 次达到设定上限并自然退出，方向导数误差 $1.31\cdot10^{-10}$ 以下。相同场中的实际 held 仍低于 .64；两侧 held guide 的终态违反约 .03193。其余五个位置 guide 与面积障碍在该独立观察为零。末段曲率独立峰 12.22972，高于强 reach 许可的粗尺度。

沿用前引 p8 场及 936 新径记录的 `hfargs`，将 p8 源文件和 p32 源分开传入。

```bash
stadium_args=(--diagonal clock-hf-diagonal-d006.json --warp clock-hf-two-material-spectral.json --warm clock-hf-full-joint-240-01.json --refined-state clock-hf-new936-ring-full-02.json --stadium stadium-p32r25-v012-H65.json --stadium-ramp stadium-p32r25-v012-H65-ramp.npz --stadium-coast stadium-p32r25-v012-H65-coast.npz --stadium-carrier stadium-new018-full-03.json)
python "$SCRIPTS/2ecf-strong-stadium-lower-slope-complete.py" "${hfargs[@]}" "${stadium_args[@]}" --prefix stadium-p32-new018-full
```

三次实际保存的状态为 `a850d935fd4de84a1fc4c9f3a429854f1b353171f428f7a7f5c396b88ccf7f2a`、`e317574c235c8f39555bd979f70a80a2750b45ea1a59b8c0f8e7c068694b0e65`、`3710fc1ed7aaecf5e0d2a92e3e787afe33e1d43cdbe63e6083e834c1ddeff9e4`。源码为 `59f1ab20e89f02aeaed9f3c5682629784175fd3052bacadafabfee7fbd5a86da`，新目标回执为 `446173fcaf12cafed4e9d8e274810f2f526da515399cdbb39230c67cd66e9f89`。
