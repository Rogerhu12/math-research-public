# CM12 完整函数与共同窗口恢复（2026-11-13 台北）

## 已完成和不可变输入

R184 证明、源码及最终证书清单在 `notes/2026-11-13-r184-stable-files.json`。CM12 完整 304 位 / 454 步固定文件替换 `scripts/data/p41_cm12_slp47_saved.json.gz`；SHA 为 `5e505ebeb3b12f2f443766177c335a9ffc91e23206d9074e7dbe27f67f45f9c2`，不要从旧 180 位重跑。完整纯整数符号/位重组、全部主截面 SHA 和最终零类维 1 已再核。

两端点 g0、gS 均是完整 73 维实际理想同构，含 v/f0；gS 的目标是 R179 CM12 transport 中 endpoints[0]。26 CM 盘最高 e=4、4 低典范盘最高 e=2；完整高102范数 2142766；碰撞范数 fC0[Du]_j=3560142/log3497834。fCS(A0)=3664450/log4870563，全部454步单位、全部54三阶 jets 相等。新第二逆完成，原 R141 同框架 λ(mC12,3mDu)=4082232；未混用新S框架。

所有新原型源码的语法问题已经修到实际 PASS；尤其共同 window norm 中 evaluate_jet 的参数必须传原 JSON，不是已转换的矩阵 pair。稳定修正源 SHA 51f0fd51a658fc06e74838e7aae308638823f9fb9fcee657dfe9e3c37b98ec39。

## 共同宽5链

源 `p41_translation_window_slp47.py` 已发布，SHA 33f1cfe0cd3f821a29f1b72682a0a1c5cb61a1648ea0a2881207b43b2f1c45d6。完整17节点预计算缓存 SHA7634c29ce0d34aa807bad3ec92bf5ac09ac5021e431122ccd047ac3fa4d0f4bd 必须与主 rolling 同用；所有预计算正负点、flip函数、RNG均已保存。精确369节点DAG最终等于m，不是binary链。先前固定 main 到282/369节点（现已由末节完整369终态替代），885479字节，SHA9bd3fd1add574a9d3041fedb6827b16e0f7dd74970ca6ab707a171e2df022992（旧180节点可从提交5d94a613恢复），后续继续写/tmp rolling。

17节点小norm证书已通过两CM实际范数与全部54×3 jets；这是输入前缀，不能说共同链已完成。完整共同fD=F/(g*hD^m)仍须369节点、R179 family1实际g、最后Norm。既有R178 hD初始Norm为CM12 229643/log3651383、CM7 1358348/log4040073。

## CM7恢复点

历史295位/440步以`p41_cm7_slp47_295_fixed.json.gz`独立保留，SHA924a49022c0ecb2b01cb9aafe705f67faa41e358affeb7bef56d7f7e748a8bf8。当前saved已替换为完整304位454步，SHAe0c0f13d9b3170d3956e0c9725d34ee300ffb22ce9542b7118e6f86539a0f024。原819行chart省略原行254，所有点/主截面已转回原基；两端点、全部碰撞范数、第一族范数与形式值均已完成，见r184-cm7增补和清单，不重跑。

## 直接重做已完成后处理

从仓库数据恢复同名 `/tmp` 输入（把CM12 saved复制为 `/tmp/p41_cm12_slp47_complete.json.gz`；R160两份实际jets及高102raw由其已发布重建脚本恢复）。不重做群链。

```sh
python scripts/p41_miller_actual_endpoint47.py --script-dir scripts --class-name cm12 --frame original --miller /tmp/p41_cm12_slp47_complete.json.gz --output /tmp/p41_cm12_endpoint47_certificate.json.gz
python scripts/p41_miller_actual_endpoint47.py --script-dir scripts --class-name cm12 --frame newS --miller /tmp/p41_cm12_slp47_complete.json.gz
python scripts/p41_cm_miller_prepared47.py --script-dir scripts --discriminant 12 --miller /tmp/p41_cm12_slp47_complete.json.gz --endpoint /tmp/p41_cm12_endpoint47_certificate.json.gz --output /tmp/p41_cm12_miller_prepared47_complete.json.gz
python scripts/p41_cm_miller_prepared47.py --script-dir scripts --discriminant 12 --jets /tmp/p41_canonical_low_jets47_raw.json.gz --miller /tmp/p41_cm12_slp47_complete.json.gz --endpoint /tmp/p41_cm12_endpoint47_certificate.json.gz --output /tmp/p41_cm12_canonical_low_prepared47_complete.json.gz
python scripts/p41_cm_canonical_high47.py --script-dir scripts --discriminant 12 --miller /tmp/p41_cm12_slp47_complete.json.gz --endpoint /tmp/p41_cm12_endpoint47_certificate.json.gz --output /tmp/p41_cm12_canonical_high47_complete.json.gz
python scripts/p41_cm_f2_leading_norm47.py --discriminant 12
python scripts/p41_cm_newS_norm_first47.py --script-dir scripts --discriminant 12
python scripts/p41_cm_translation_formal_height47.py --script-dir scripts --target 12
```

共同norm前缀不做群运算：

```sh
python scripts/p41_translation_window_norms47.py --script-dir scripts --miller scripts/data/p41_translation_window47_17_fixed.json.gz --build scripts/data/p41_translation_build47_complete.json.gz --output /tmp/p41_translation_window_norms47_17_fixed.json.gz
```

完整common后改为369固定文件，并传 `--endpoint` 为 `p41_miller_actual_endpoint47.py --class-name common` 生成的实际证书。原R178 initial_norms输入取仓库已发小证书，函数值仍必须减 g 和 hD^m。

## 数学边界与下一项

R183 root已算CM12 T2范数4551951/log1585263、rhoT log2361421、FΣ log3375352。最终用R184式(184.15)，只在实际共同fD范数完成后才能完整组装并乘800；s_u使用g1规范698837/log152280。CM7同项已完成，T2范数945641/log2692959，全部表见R183§8及CM7增补；仍不能把两个F2输入当作全部54条CM校准或全部QC根排除。root独占tracked/git，本支继续/tmp计算；所有有意义完成态发root普通终端push保存。

原driver在282步之后exit137；原样重载亦被终止，无新增节点。已用低峰值continuation从282原RNG和同一DAG恢复；它先释放JSON、仅加载实际所需8缓存点，原17缓存不变。后续新增源码/完成边界另存，不将进程存在当作节点完成。

## 共同369节点完成

低内存续算已完成全部369节点，saved现为1117830字节、SHA d8c81ce88340383955eb48965ef51b218fca39f65e39d663de4767b27e8fbdbf；最终实际指数恰m，360 AddFlip与9 flip全保存，约化零类维1。最终点SHA8add393932e8a0cbda933fa8824b57a0eecc94a8dc15ce64e06a999e1ac3c555。原282输入以p41_translation_window47_282_fixed.json.gz固定保留，因为continuation直接绑定其SHA；原17缓存不动。续算脚本scripts/p41_translation_window_finish47.py必须传--original-driver scripts/p41_translation_window_slp47.py以吻合实际导入源。完整Db端点、范数及两个F2汇总另见同日R184最终高度增补；勿再跑共同群链。
