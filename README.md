# Figura Studio — Free Model Workshop

เว็บสร้างโมเดล Minecraft / Figura แบบ Cube และ Pixel Texture ด้วยเครื่องมือฟรี ไม่ต้องมี API key

## เปิดเว็บไซต์

เมื่อเปิด GitHub Pages ของ repository นี้แล้ว เว็บไซต์จะอยู่ที่:

**https://ismyp12-wq.github.io/Model/**

เปิด GitHub Pages (ทำครั้งเดียว):
1. ไปที่ https://github.com/ismyp12-wq/Model/settings/pages
2. เลือก **Build and deployment → Source: Deploy from a branch**
3. เลือก **main** และ **/(root)** จากนั้นกด **Save**
4. หลัง GitHub Pages แสดงสถานะเผยแพร่สำเร็จ ให้เปิด URL ข้างต้น

## ความสามารถ

- สร้างโมเดล Cube จากแม่แบบและคำบรรยายอย่างง่าย (ไม่ใช่โมเดล AI)
- แก้ Cube: ตำแหน่ง ขนาด สี คัดลอก กระจกเงา และ Undo/Redo
- ดูตัวอย่าง 3D หมุนและซูมด้วย Canvas
- วาด Texture 16×16 และนำเข้ารูป PNG/JPG
- เปลี่ยนภาพให้เป็น Pixel Relief แบบ Cube
- นำเข้า OBJ และ voxelize ผิวโดยประมาณ
- ส่งออก Generic .bbmodel, OBJ, PNG หรือ JSON
- จัดการหลายโปรเจกต์และบันทึกอัตโนมัติใน localStorage

## การเก็บข้อมูล

ข้อมูลถูกบันทึก **เฉพาะเบราว์เซอร์และอุปกรณ์ที่ใช้** ไม่ใช่ใน GitHub และไม่ซิงก์ข้ามเครื่อง/เว็บไซต์
การเปลี่ยนจาก https://ismyp12-wq.github.io/Deck/figura-studio/ มาเป็น https://ismyp12-wq.github.io/Model/ จะไม่โอน localStorage อัตโนมัติ
ให้กด **สำรองข้อมูลทั้งหมด** ในเว็บเก่า แล้ว **นำเข้าข้อมูลสำรอง** ในเว็บใหม่
สำรอง JSON เป็นประจำ และหลีกเลี่ยงโหมดไม่ระบุตัวตน

## ข้อจำกัด

AI image-to-3D และ text-to-mesh ไม่รวมในรุ่นฟรีนี้ การสร้างจากข้อความใช้ procedural presets เท่านั้น
OBJ-to-Cube เป็นการประมาณรูปร่างและไม่คง Texture/Rig/Animation ครบถ้วน
ควรตรวจไฟล์ .bbmodel ใน Blockbench และทดสอบประสิทธิภาพใน Figura ก่อนนำไปขาย

ไฟล์เว็บไซต์หลักคือ [index.html](./index.html) และทำงานโดยไม่มี external libraries
